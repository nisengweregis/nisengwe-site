from django.db import models

# Create your models here.


class Consulting(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.CharField(max_length=2083)

