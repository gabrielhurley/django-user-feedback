from django.db import models
from django.contrib.auth.models import User

class Feedback(models.Model):
    feedback = models.TextField()
    user = models.ForeignKey(User, null=True, blank=True, editable=False)
    url = models.URLField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    resolved = models.BooleanField(default=False)
    publish = models.BooleanField(default=False)

    class Meta:
        ordering = ['-timestamp',]
        verbose_name_plural = "Feedback"

    def __unicode__(self):
        return "Feedback from %s sent %s" % (self.user, self.timestamp,)
