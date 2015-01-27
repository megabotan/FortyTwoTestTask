from django.shortcuts import render_to_response

from models import Person


def index(request):
    person = Person.objects.all()[0]
    return render_to_response('index.html', {'person':person})
