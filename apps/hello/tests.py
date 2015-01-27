from django.test import TestCase
from django.core.urlresolvers import reverse

from hello.models import Person


class HttpTest(TestCase):
    def setUp(self):
        self.person = Person.objects.all()[0]

    def test_home(self):
        response = self.client.get(reverse('hello.views.index'))
        self.assertContains(response, self.me.name)
        self.assertContains(response, self.me.last_name)
        self.assertContains(response,
            self.me.date_of_birth.strftime('%B %d, %Y'))
        for string in self.me.bio.splitlines():
            self.assertContains(response, string)
        self.assertContains(response, self.me.email)
        self.assertContains(response, self.me.jabber)
        self.assertContains(response, self.me.skype)
        for string in self.me.other_contacts.splitlines():
            self.assertContains(response, string)