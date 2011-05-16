from feedback.forms import FeedbackForm

def feedback_form(request):
    return {'feedback_form': FeedbackForm()}
