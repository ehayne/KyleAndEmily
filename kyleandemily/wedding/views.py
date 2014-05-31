from datetime import date

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response

WEDDING_DATE = date(2015, 04, 10)

def home(request):

    today = date.today()  # TODO: uses UTC date, needs to use local timezone date

    time_until_wedding = WEDDING_DATE - today

    template = loader.get_template('home.html')
    context = RequestContext(request, {
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
    img_list = [{'img_path': 'wedding/img/vinyard.jpg',
    		 'img_text': 'Our first trip to Driftwood Vinyards where Kyle later proposed!'},
    		 {'img_path': 'wedding/img/engaged.jpg',
    		 'img_text': 'Right after Kyle proposed!'},
    ]

    template = loader.get_template('gallery.html')
    context = RequestContext(request, {
        'img_list': img_list,
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
