from django.db import models

# Create your models here.
class todoTask(models.Model):
    content = models.TextField()