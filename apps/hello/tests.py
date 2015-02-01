from django.test import TestCase
from django.core.urlresolvers import reverse
from django.conf import settings

from hello.models import Person


class HttpTest(TestCase):
    def setUp(self):
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

