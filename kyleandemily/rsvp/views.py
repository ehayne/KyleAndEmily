from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render_to_response, HttpResponseRedirect
from django.template import RequestContext
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

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
    # TODO: strip leading/trailing spaces
    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')

    person = Person.objects.get(first_name__iexact=first_name,
                                last_name__iexact=last_name)

    # TODO: capture errors here? right now we're throwing an error when a name isn't found but we need to handle that since that is a real possibility.
    #  what is iexact doing?

    context = {
        'invitation': person.invitation,
    }

    if person.invitation.responded:
        template = 'responded.html'
    else:
        template = 'rsvp.html'

    return render_to_response(template, context, RequestContext(request))

def save(request):
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
        person.save()
        index += 1

    if invitation.plusOne:
        additional_guest = request.POST['plus_one_attending']
        if additional_guest == '1':
            plusOne = Person.objects.create(invitation=invitation,
                                    attendingWedding= True,
                                    first_name=request.POST['plus_one_first_name'],
                                    last_name=request.POST['plus_one_last_name']
                                    )
            plusOne.save()

    invitation.responded = True
    invitation.comment = request.POST.get('comment')
    invitation.save()

    plaintext = get_template('email.txt')
    htmly = get_template('email.html')

    d = Context({ 'invitation': person.invitation })

# TODO: re-enable email, currently disabled for working locally - should probably add a switch for this?
#     subject, from_email, to = '[RSVP] Wedding RSVP Received', 'donotreply8386@gmail.com', 'buschang.rockman.wedding@gmail.com'
#     text_content = plaintext.render(d)
#     html_content = htmly.render(d)
#     msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
#     msg.attach_alternative(html_content, "text/html")
#     msg.send()

    context = {
        'invitation': person.invitation,
    }
    template = 'responded.html'

    return render_to_response(template, context, RequestContext(request))