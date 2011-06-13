from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

FEEDBACK_TYPES = (
    ('bug', 'Bug'),
    ('feature', 'Feature'),
    ('support', 'Support request'),
)

class Feedback(models.Model):
    feedback = models.TextField()
    user = models.ForeignKey(User, null=True, blank=True)
    url = models.URLField(blank=True, verify_exists=False)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    resolved = models.BooleanField(default=False)
    publish = models.BooleanField(default=False)
    type = models.CharField(max_length=128, blank=True, choices=getattr(settings, 'FEEDBACK_TYPES', FEEDBACK_TYPES))

    class Meta:
        ordering = ['-timestamp',]
        verbose_name_plural = "Feedback"

    def __unicode__(self):
        return "Feedback from %s sent %s" % (self.user, self.timestamp,)
