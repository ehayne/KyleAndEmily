from datetime import date, datetime

from django.http import HttpResponse
from django.template import RequestContext, loader
# from django.shortcuts import render_to_response
from photologue.models import Photo
from pytz import timezone

WEDDING_DATE = datetime(2014, 06, 13, 14 ,0 ,0, 0, timezone('US/Central'))

def home(request):

    now_utc = datetime.now(timezone('UTC'))
    now_central = now_utc.astimezone(timezone('US/Central'))

    time_until_wedding = WEDDING_DATE - now_central
    days, hours, mins = (time_until_wedding.days,
                         time_until_wedding.seconds//3600,
                         (time_until_wedding.seconds//60)%60)
    
    married = mins < 1
        

    template = loader.get_template('home.html')
    context = RequestContext(request,
    {
        'days_left': days,
        'hours_left': hours,
        'mins_left': mins,
        'is_married': married
    })
    return HttpResponse(template.render(context))

def about(request):
    template = loader.get_template('about.html')
    context = RequestContext(request, {
        'latest_question_list': 'x',
    })
    return HttpResponse(template.render(context))


def gallery(request):

    wedding_photos = Photo.objects.on_site().is_public()

    template = loader.get_template('gallery.html')
    context = RequestContext(request, {
        'object_list': wedding_photos,
    })
    return HttpResponse(template.render(context))


def details(request):
    template = loader.get_template('details.html')
    context = RequestContext(request, {
        'latest_question_list': 'x',
    })
    return HttpResponse(template.render(context))

def hotels(request):
    template = loader.get_template('hotels.html')
    context = RequestContext(request, {
        'latest_question_list': 'x',
    })
    return HttpResponse(template.render(context))

def rsvp(request):
    template = loader.get_template('rsvp.html')
    context = RequestContext(request, {
        'latest_question_list': 'x',
    })
    return HttpResponse(template.render(context))

def registry(request):
    template = loader.get_template('registry.html')
    context = RequestContext(request, {
        'latest_question_list': 'x',
    })
    return HttpResponse(template.render(context))
