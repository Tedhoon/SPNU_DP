from django.db import models

class DeliveryList(models.Model):
    title = models.CharField(max_length=100)
    notion = models.CharField(max_length=300)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    menu = models.TextField()
    description = models.CharField(max_length = 150)

    def __str__(self):
        return self.title

class DeliveryGroup(models.Model):
    pass

class DeliveryService(models.Model):
    pass
    