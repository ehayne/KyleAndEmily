from datetime import datetime

from django.http import HttpResponse
from django.template import RequestContext, loader
from photologue.models import Gallery
from pytz import timezone

from kyleandemily.site_text import (ABOUT_TEXT,
                                  DETAILS_TEXT,
                                  HOTEL_TEXT,
                                  WEDDING_DATE,
                                  ENGAGEMENT_DATE)



def home(request):


    today = datetime.now(tz=timezone('US/Central'))

    time_until_wedding = WEDDING_DATE - today
    days, hours, mins = (time_until_wedding.days,
                         time_until_wedding.seconds//3600,
                         (time_until_wedding.seconds//60)%60)

    married = WEDDING_DATE < today


    template = loader.get_template('home.html')
    context = RequestContext(request,
    {
        'days_left': days,
        'hours_left': hours,
        'mins_left': mins,
        'is_married': married,
    },)

    return HttpResponse(template.render(context))


def about(request):

    template = loader.get_template('about.html')
    context = RequestContext(request,
    {
        'about_groom': ABOUT_TEXT['about_groom'],
        'about_bride': ABOUT_TEXT['about_bride'],
        'how_we_met': ABOUT_TEXT['how_we_met'],
        'engagement_story': ABOUT_TEXT['engagement_story'],
        'engagement_date': ENGAGEMENT_DATE,
    })
    return HttpResponse(template.render(context))


def gallery(request):

    wedding_photos = Gallery.objects.filter(tags='wedding')

    template = loader.get_template('gallery.html')
    context = RequestContext(request, {
        'object_list': wedding_photos,
    })
    return HttpResponse(template.render(context))


def instagram(request):

    template = loader.get_template('instagram.html')
    context = RequestContext(request, {
        'object_list': None,
    })
    return HttpResponse(template.render(context))


def details(request):
    template = loader.get_template('details.html')
    context = RequestContext(request, {
        'ceremony': DETAILS_TEXT['ceremony'],
        'reception': DETAILS_TEXT['reception'],
        'dress_code': DETAILS_TEXT['dress_code'],
        'directions_text': DETAILS_TEXT['driving_directions_text'],
        'map_url': DETAILS_TEXT['map_url'],
    })
    return HttpResponse(template.render(context))


def hotels(request):
    template = loader.get_template('hotels.html')
    context = RequestContext(request, {
        'accomodations_text': HOTEL_TEXT['accomodations_text'],
    })
    return HttpResponse(template.render(context))


def rsvp(request):
    template = loader.get_template('rsvp.html')
    context = RequestContext(request, {
        'extra_css_file': ['rsvp/css/rsvp.css', ],
    })
    return HttpResponse(template.render(context))


def registry(request):
    template = loader.get_template('registry.html')
    context = RequestContext(request, {
        'latest_question_list': 'x',
    })
    return HttpResponse(template.render(context))
