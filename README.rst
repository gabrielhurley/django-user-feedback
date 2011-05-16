====================
Django User Feedback
====================

A simple Django application for collecting feedback from users.

Requirements
============

  * Django 1.3+ (uses class-based views)
  * Python 2.5+

Quick Start
===========

Step 1: INSTALLED_APPS
----------------------

Add ``feedback`` to your ``INSTALLED_APPS`` setting.

Step 2: URLconf
----------------------

Add ``url(r'^feedback/', include('feedback.urls')),`` to your ``urls.py``.

Step 3: Context Processor
-------------------------

For sitewide availability of the feedback form there is a handy middleware
``feedback.context_processors.feedback_form`` which can be added to your
``TEMPLATE_CONTEXT_PROCESSORS`` setting. If you choose not to use this
middleware you will need to manually provide a ``feedback_form`` variable
in your context.

Step 4: Templates
-----------------

You will need to include your feedback form somewhere on the site. There are
included form and page templates at ``feedback/form.html`` and
``feedback/feedback.html`` respectively. They are intentionally as simple as
possible. You will almost certainly want to customize them, but they provide
a viable starting point.

OPTIONS
=======

There are a few optional settings available:

``FEEDBACK_SEND_EMAIL``

    Default: False. If set to True, an email will be sent each time a user
    provides feedback.

``FEEDBACK_EMAIL_TO``

    Default: ``settings.DEFAULT_FROM_EMAIL``. The email address to which
    feedback emails should be sent.

There are also two additional templates ``feedback/email/body.txt`` and
``feedback/email/subject.txt`` which control the output formatting for the
email messages.
