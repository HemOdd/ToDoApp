from django.db import models
from todoapp.validators import validate_is_zip_or_image

# Create your models here.
class todoTask(models.Model):
    content = models.TextField()

class fileModel(models.Model):
    mediaFile = models.FileField(upload_to='uploadedFiles/', validators = [validate_is_zip_or_image])

