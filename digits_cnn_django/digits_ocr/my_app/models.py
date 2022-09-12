from django.db import models
from django import forms

# Create your models here. 
class ImagefieldModel(models.Model): 
    title = models.CharField(max_length = 200) 
    img = models.ImageField(upload_to = "images/")

    class Meta:
        db_table = "imageupload"