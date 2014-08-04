from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext


def index(request):
    context = RequestContext(request)

    context_dict = {'bold_message': 'This is a message to be bolded'}

    return render_to_response('clients/template1.html', context_dict, context)
