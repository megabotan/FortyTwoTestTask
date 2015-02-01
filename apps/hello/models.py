from django.db import models
from django.conf import settings
from PIL import Image, ImageOps


class Person(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    bio = models.TextField()
    email = models.EmailField()
    jabber = models.CharField(max_length=200)
    skype = models.CharField(max_length=200)
    other_contacts = models.TextField()
    photo = models.ImageField(
        upload_to='images',
        default='default.jpg',
        null=True)

    def save(self):
        if not self.photo:
            return
        super(Person, self).save()
        image = Image.open(self.photo)
        size = settings.PHOTO_SIZE
        image.thumbnail(size, Image.ANTIALIAS)
        background = Image.new('RGBA', size, (255, 255, 255, 0))
        background.paste(
            image,
            ((size[0] - image.size[0]) / 2, (size[1] - image.size[1]) / 2))
        background.save(self.photo.path)


class Request(models.Model):
    url = models.CharField(max_length=200)
    method = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)