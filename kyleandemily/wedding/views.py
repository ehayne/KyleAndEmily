from datetime import date

from django.http import HttpResponse
from django.template import RequestContext, loader
# from django.shortcuts import render_to_response
from photologue.models import Photo

WEDDING_DATE = date(2015, 04, 10)

def home(request):

    today = date.today()  # TODO: uses UTC date, needs to use local timezone date

    time_until_wedding = WEDDING_DATE - today

    template = loader.get_template('home.html')
    context = RequestContext(request, {
        'js_file': ['/static/base/js/main.js']
    },
    {
        'days_left': time_until_wedding.days,
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
