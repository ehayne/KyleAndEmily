from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response



def home(request):
    template = loader.get_template('home.html')
    context = RequestContext(request, {
        'latest_question_list': 'x',
    })
    return HttpResponse(template.render(context))

def about(request):
    template = loader.get_template('about.html')
    context = RequestContext(request, {
        'latest_question_list': 'x',
    })
    return HttpResponse(template.render(context))


def gallery(request):
    template = loader.get_template('gallery.html')
    context = RequestContext(request, {
        'latest_question_list': 'x',
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
