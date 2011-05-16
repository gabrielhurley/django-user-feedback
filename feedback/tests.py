import time

from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.template import Template, RequestContext
from django.test import TestCase
from django.test.client import Client, RequestFactory

from feedback.models import Feedback

class FeedbackTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            unicode(int(time.time())),
            'example@example.com',
            'insecure'
        )
        self.data = {
            "feedback": "Your site is great.",
        }
        self.c = Client()
        self.feedback_url = reverse('django-user-feedback')

    def test_feedback_submission(self):
        response = self.c.post(self.feedback_url, self.data)
        feedback1 = Feedback.objects.latest('id')
        self.assertEqual(self.data['feedback'], feedback1.feedback)
        self.assertTrue(self.c.login(username=self.user.username, password='insecure'))
        response = self.c.post(self.feedback_url, self.data)
        feedback2 = Feedback.objects.latest('id')
        self.assertNotEqual(feedback1.id, feedback2.id)
        self.assertEqual(self.user.id, feedback2.user.id)

    def test_context_processor(self):
        OLD_TEMPLATE_CONTEXT_PROCESSORS = settings.TEMPLATE_CONTEXT_PROCESSORS
        settings.TEMPLATE_CONTEXT_PROCESSORS = tuple(settings.TEMPLATE_CONTEXT_PROCESSORS) + ('feedback.context_processors.feedback_form',)
        request = self.factory.get(self.feedback_url)
        c = RequestContext(request)
        self.assertTrue(c.has_key('feedback_form'))
        response = self.c.post(self.feedback_url, {})
        self.assertEqual(1, len(response.context['feedback_form'].errors))
        settings.TEMPLATE_CONTEXT_PROCESSORS = OLD_TEMPLATE_CONTEXT_PROCESSORS