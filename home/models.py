from django.db import models
from django.utils import timezone

class Contact(models.Model):
    name= models.CharField(max_length=122, null=True)
    email= models.CharField(max_length=122, null=True)
    phone= models.CharField(max_length=122, null=True)
    desc= models.TextField( null=True)
    date= models.DateField( null=True)
    def __str__(self):
        return self.name

# Create your models here.
