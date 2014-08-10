from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from clients.models import Client

def index(request):
    context = RequestContext(request)

    client_list = Client.objects.all()
    client_dict = {'clients': client_list}

    return render_to_response('clients/index.html', client_dict, context)


def clientView(request, client_id):
    context = RequestContext(request)

    client = Client.objects.get(id=client_id)
    context_dict = {'client': client}

    return render_to_response('clients/client.html', context_dict, context)
