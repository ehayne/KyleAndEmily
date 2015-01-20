from __future__ import absolute_import

from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template, render_to_string
from django.template import Context
from kyleandemily import settings


@shared_task
def send_email(context={}, subject_text='', body_text_template='',
    body_html_template='', from_email=settings.DEFAULT_FROM_EMAIL, to_email=settings.DEFAULT_TO_EMAIL):

    # render content
    d = Context(context)
    body_text = get_template(body_text_template).render(d)
    body_html = get_template(body_html_template).render(d)

    # send email
    email = EmailMultiAlternatives(subject_text, body_text, from_email, [to_email])
    email.attach_alternative(body_html, "text/html")
    email.send()