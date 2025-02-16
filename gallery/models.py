from django.db import models


class Gallery(models.Model):
    image = models.FileField(upload_to='my_gallery')
