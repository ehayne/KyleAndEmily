from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response



def home(request):
    return HttpResponse("Hello, world. You're at the home page.")

def about(request):
    template = loader.get_template('about.html')
    context = RequestContext(request, {
        'latest_question_list': 'x',
    })
    return HttpResponse(template.render(context))

def details(request):
    return HttpResponse("Hello, world. You're at the details page.")

def hotels(request):
    return HttpResponse("Hello, world. You're at the hotels page.")

def rsvp(request):
    return HttpResponse("Hello, world. You're at the rsvp page.")

def registry(request):
    return HttpResponse("Hello, world. You're at the registry page.")
