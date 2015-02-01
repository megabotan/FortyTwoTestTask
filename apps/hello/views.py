from django.shortcuts import render_to_response
from django.conf import settings

from models import Person, Request


def index(request):
    person = Person.objects.all()[0]
    return render_to_response('index.html', {'person': person})


def requests(request):
    count = settings.REQUESTS_ON_PAGE
    requests = Request.objects.all().order_by('date')[:count]
    return render_to_response('requests.html', {'requests': requests})