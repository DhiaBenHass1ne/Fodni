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
    bio = models.CharField(blank=True, null=True)
    category = models.ForeignKey('Category', related_name='provider_category', on_delete=models.CASCADE , blank=True, null=True)
    # image  = models.ImageField(upload_to='static/')


    def __str__(self):
        return str(self.user)
    
class City(models.Model):
    gov = models.CharField(max_length=500)
    state = models.CharField(max_length=500)


    def __str__(self):
        return self.name

class Category(models.Model):
    title=models.CharField(max_length=200)
    description= models.TextField()

class Post(models.Model):
    author = models.ForeignKey (User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description= models.TextField()
    post_category = models.ForeignKey (Category, on_delete=models.CASCADE,default="Other")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + "/n" + self.description
    

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    provider= models.ForeignKey(Provider, on_delete=models.CASCADE)
    rating = models.FloatField() 
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'provider']
        
    def __str__(self):
        return f'{self.user.username} - {self.rating} stars'