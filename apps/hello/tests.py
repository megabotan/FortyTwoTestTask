from django.test import TestCase
from django.core.urlresolvers import reverse

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