from __future__ import absolute_import

from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template, render_to_string
from django.template import Context
from kyleandemily import settings


@shared_task
def send_rsvp_email(response):
    print('in email')
    plaintext = get_template('email.txt')
    htmly = get_template('email.html')

    d = Context({ 'invitation': response })

    subject, from_email, to = ('[RSVP] Wedding RSVP Received',
                               'donotreply8386@gmail.com',
                               'buschang.rockman.wedding@gmail.com')
    text_content = plaintext.render(d)
    html_content = htmly.render(d)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

@shared_task
def send_email(email, context={}, subject_template='', body_text_template='',
    body_html_template='', from_email=settings.DEFAULT_FROM_EMAIL):

    # render content
    subject = render_to_string([subject_template], context).replace('\n', ' ')
    body_text = render_to_string([body_text_template], context)
    body_html = render_to_string([body_html_template], context)

    # send email
    email = EmailMultiAlternatives(subject, body_text, from_email, [email])
    email.attach_alternative(body_html, 'text/html')
    email.send()