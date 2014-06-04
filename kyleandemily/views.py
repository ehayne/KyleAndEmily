from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response



def under_construction(request):
    template = loader.get_template('under_construction.html')
    context = RequestContext(request, {
        'latest_question_list': 'x',
    })
    return HttpResponse(template.render(context))

