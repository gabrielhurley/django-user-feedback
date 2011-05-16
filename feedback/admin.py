from django.contrib import admin

from feedback.models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    list_display = ('user', 'feedback', 'timestamp', 'resolved', 'publish')
    list_editable = ('resolved', 'publish')
    list_filter = ('user', 'resolved', 'publish')
    search_fields = ['feedback', 'user']

admin.site.register(Feedback, FeedbackAdmin)