from django.db import models


# Create your models here.

class PathFolder(models.Model):
    path_to_folder = models.CharField(max_length=200)
