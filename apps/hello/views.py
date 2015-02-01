import os

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, get_object_or_404
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from models import Person, Request
from forms import PersonForm


def index(request):
    person = Person.objects.all()[0]
    return render(request, 'index.html', {'person': person})


def requests(request):
    count = settings.REQUESTS_ON_PAGE
    requests = Request.objects.all().order_by('date')[:count]
    return render_to_response('requests.html', {'requests': requests})


@login_required
def edit(request):
    person = get_object_or_404(Person)
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form = PersonForm(request.POST, request.FILES, instance=person)
            form.save()
            clear_images_folder(person.photo)
            return HttpResponseRedirect(reverse('hello.views.index'))
    else:
        form = PersonForm(instance=person)
    return render(request, 'edit.html', {
        'form': form,
        'person': person
    })


def clear_images_folder(actual_photo):
    folder = os.path.join(settings.MEDIA_ROOT, 'images/')
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        if (os.path.isfile(file_path) and
           the_file != os.path.basename(actual_photo.path)):
            os.unlink(file_path)