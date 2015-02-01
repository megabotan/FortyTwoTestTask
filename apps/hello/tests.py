import datetime

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.conf import settings
from django.test.client import Client

from hello.models import Person


class HttpTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.person = Person.objects.all()[0]

    def test_home(self):
        response = self.client.get(reverse('hello.views.index'))
        self.assertContains(response, self.person.name)
        self.assertContains(response, self.person.last_name)
        self.assertContains(response,
            self.person.date_of_birth.strftime('%B %d, %Y'))
        for string in self.person.bio.splitlines():
            self.assertContains(response, string)
        self.assertContains(response, self.person.email)
        self.assertContains(response, self.person.jabber)
        self.assertContains(response, self.person.skype)
        for string in self.person.other_contacts.splitlines():
            self.assertContains(response, string)

    def test_requests(self):
        urls = ['/almost_random_string_{0}'.format(i)
                for i in range(settings.REQUESTS_ON_PAGE + 1)]
        for url in urls:
            response = self.client.get(url)
        response = self.client.get(reverse('hello.views.requests'))
        for url in urls[:-1]:
            self.assertContains(response, url)
        self.assertNotContains(response, urls[-1])

    def test_edit_page(self):
        response = self.client.get(reverse('hello.views.edit'))
        self.assertRedirects(response, '/login/')
        self.assertTrue(c.login(username='admin', password='admin'))
        response = self.client.get(reverse('hello.views.edit'))
        self.assertTemplateUsed(response, 'edit.html')
        new_data = {'name': 'John',
                    'last_name': 'Smith',
                    'date_of_birth': datetime.datetime.now(),
                    'bio': 'test bio',
                    'email': 'email@email.com',
                    'jabber': 'jabber@jabber.com',
                    'skype': 'test_skype',
                    'other_contacts': 'test other_contacts',
                    }
        self.client.post(reverse('hello.views.edit'), new_data)
        response = self.client.get(reverse('hello.views.index'))
        for value in new_data.itervalues():
            assertContains(response, value)


class ContextTest(TestCase):
    def test_template_context_processor(self):
        response = self.client.get('/almost_random_string')
        self.assertTrue('settings' in response.context)
        self.assertEquals(response.context['settings'], settings)
