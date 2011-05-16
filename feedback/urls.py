from django.conf.urls.defaults import patterns, url

from feedback.views import FeedbackView

urlpatterns = patterns('feedback.views',
    url(r'^$', FeedbackView.as_view(), name='django-user-feedback')
)