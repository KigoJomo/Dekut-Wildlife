from django.db import models

class Official(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    phone = models.BigIntegerField(null=True)
    pic = models.ImageField(upload_to='images', null=True)

