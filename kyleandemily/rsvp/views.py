from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from kyleandemily import settings

from kyleandemily.rsvp.tasks import send_email

from .models import Person, Invitation


class DotExpandedDict(dict):
    """
A special dictionary constructor that takes a dictionary in which the keys
may contain dots to specify inner dictionaries. It's confusing, but this
example should make sense.

>>> d = DotExpandedDict({'person.1.firstname': ['Simon'], \
'person.1.lastname': ['Willison'], \
'person.2.firstname': ['Adrian'], \
'person.2.lastname': ['Holovaty']})
>>> d
{'person': {'1': {'lastname': ['Willison'], 'firstname': ['Simon']}, '2': {'lastname': ['Holovaty'], 'firstname': ['Adrian']}}}
>>> d['person']
{'1': {'lastname': ['Willison'], 'firstname': ['Simon']}, '2': {'lastname': ['Holovaty'], 'firstname': ['Adrian']}}
>>> d['person']['1']
{'lastname': ['Willison'], 'firstname': ['Simon']}

# Gotcha: Results are unpredictable if the dots are "uneven":
>>> DotExpandedDict({'c.1': 2, 'c.2': 3, 'c': 1})
{'c': 1}
"""
    def __init__(self, key_to_list_mapping):
        for k, v in key_to_list_mapping.items():
            current = self
            bits = k.split('.')
            for bit in bits[:-1]:
                current = current.setdefault(bit, {})
            # Now assign value to current position
            try:
                current[bits[-1]] = v
            except TypeError: # Special-case if current isn't a dict.
                current = {bits[-1]: v}


def landing(request):

    context = RequestContext(request, {
        'msg': '',
    })

    return render_to_response('entry.html', context, RequestContext(request))



def lookup(request):
    """
    find RSVP entry and direct user to appropriate template based on response status
    """
    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')

    person = Person.objects.get(first_name__iexact=first_name.strip(),
                                last_name__iexact=last_name.strip())

    context = {
        'invitation': person.invitation,
    }

    if person.invitation.responded:
        template = 'responded.html'
    else:
        template = 'rsvp.html'

    return render_to_response(template, context, RequestContext(request))

def save(request):
    """
    validate response, save it and send email to let couple know about response
    """
    invitation = get_object_or_404(
        Invitation,
        id=request.POST['invitation_id']
    )

    persons = DotExpandedDict(request.POST)

    index = 0
    for person in invitation.people.all():
        def p_attr(name):
            "Closure to make getting attrs from persons easier"
            return persons['person'][str(index)][name]

        person.attendingWedding = True if p_attr('attendingWedding') == '1' else False
        person.attendingWelcome = True if p_attr('attendingWelcome') == '1' else False
        person.attendingFarewell = True if p_attr('attendingFarewell') == '1' else False
        person.first_name = p_attr('first_name')
        person.last_name = p_attr('last_name')

        if not person.first_name or not person.last_name:
            context = {
            'invitation': invitation,
            'error_msg': 'I''m sorry but there was an error.  Please confirm your response and try again.',
            }
            template = 'rsvp.html'

            return render_to_response(template, context, RequestContext(request))

        person.full_clean()
        person.save()
        index += 1

    if invitation.plusOne:
        add_plus_one = request.POST['addPlusOne']

        if add_plus_one == '1':

            plus_one_first_name = request.POST['plus_one_first_name']
            plus_one_last_name = request.POST['plus_one_last_name']

            if not plus_one_first_name or not plus_one_last_name:
                context = {
                'invitation': invitation,
                'error_msg': 'I''m sorry but there was an error.  Please confirm your response and try again.',
                }

                template = 'rsvp.html'

                return render_to_response(template, context, RequestContext(request))
            plusOne = Person.objects.create(invitation=invitation,
                                            first_name=plus_one_first_name,
                                            last_name=plus_one_last_name,
                                            attendingWedding=request.POST['plus_one_attending'],
                                            attendingWelcome=request.POST['plusOneAttendingWelcome'],
                                            attendingFarewell=request.POST['plusOneAttendingFarewell'],
                                            plusOneSwitch=True,
                                    )

            plusOne.full_clean()
            plusOne.save()

    invitation.responded = True
    invitation.comment = request.POST.get('comment')
    invitation.full_clean()
    invitation.save()

    context = {
        'invitation': person.invitation
    }

    subject = '[RSVP] Wedding RSVP Received'
    send_email.delay(context=context, subject_text=subject, body_text_template='email.txt',
                     body_html_template='email.html', from_email=settings.DEFAULT_FROM_EMAIL,
                     to_email=settings.DEFAULT_TO_EMAIL)

    template = 'responded.html'

    return render_to_response(template, context, RequestContext(request))