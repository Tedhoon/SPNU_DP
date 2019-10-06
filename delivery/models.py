from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class DeliveryList(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    text = RichTextUploadingField(null = True, blank =True)


    def __str__(self):
        return self.title