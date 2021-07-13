from django.db import models

# Create your models here.
class Carousel(models.Model):
    title = models.CharField(max_length=100)
    short_desc = models.TextField()
    thumbnail = models.ImageField(upload_to='public/')
    description = models.TextField()


# Create your models here.
class Freature(models.Model):
    post = models.CharField(max_length=100)
    image = models.ImageField(upload_to='public/')
    description = models.TextField()


