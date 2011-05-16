from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template import RequestContext
from django.template.loader import render_to_string
from django.views.generic import CreateView

from feedback.utils import send_threaded
from feedback.forms import FeedbackForm
from feedback.models import Feedback

class FeedbackView(CreateView):
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'

    def get_form_kwargs(self):
        kwargs = super(FeedbackView, self).get_form_kwargs()
        instance = Feedback(
            url = self.request.META.get("HTTP_REFERER", ''),
            user = self.request.user if self.request.user.is_authenticated() else None
        )
        kwargs.update({
            "instance": instance,
        })
        return kwargs

    def form_valid(self, *args, **kwargs):
        if getattr(settings, 'FEEDBACK_SEND_EMAIL', False):
            context = {"feedback":self.object}
            send_threaded(EmailMultiAlternatives(
                    render_to_string('feedback/emails/feedback_subject.txt', context),
                    render_to_string('feedback/emails/feedback_body.txt', context),
                    settings.DEFAULT_FROM_EMAIL,
                    [getattr(settings, 'FEEDBACK_TO_EMAIL', settings.DEFAULT_FROM_EMAIL),]
                )
            )
        if 'django.contrib.messages' in settings.INSTALLED_APPS:
            messages.success(self.request, "Your feedback has been sent. Thank you!")
        return super(FeedbackView, self).form_valid(*args, **kwargs)

    def form_invalid(self, form):
        # Update our context to avoid being overwritten by context processors
        context = RequestContext(self.request, self.get_context_data())
        context['feedback_form'] = form
        return self.render_to_response(context)

    def get_success_url(self):
        return self.request.META.get("HTTP_REFERER", reverse('django-user-feedback'))
