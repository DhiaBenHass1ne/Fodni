from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey('City', related_name='client_city', on_delete=models.CASCADE , blank=True, null=True)
    # image  = models.ImageField(upload_to='static/')


    def __str__(self):
        return str(self.user)

class Provider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey('City', related_name='provider_city', on_delete=models.CASCADE , blank=True, null=True)
    # image  = models.ImageField(upload_to='static/')


    def __str__(self):
        return str(self.user)
    
class City(models.Model):
    gov = models.CharField(max_length=500)
    state = models.CharField(max_length=500)


    def __str__(self):
        return self.name

