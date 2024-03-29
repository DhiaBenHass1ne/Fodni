from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey('City', related_name='client_city', on_delete=models.CASCADE , blank=True, null=True)
    phone = models.CharField(max_length=8,null=True)
    image = models.ImageField(upload_to='clients/',null=True)


    def __str__(self):
        return str(self.user)

class Provider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey('City', related_name='provider_city', on_delete=models.CASCADE , blank=True, null=True)
    phone = models.CharField(max_length=8,null=True)
    bio = models.CharField(blank=True, null=True)
    category = models.ForeignKey('Category', related_name='provider_category', on_delete=models.CASCADE , blank=True, null=True)
    image = models.ImageField(upload_to='providers/', null=True)
    active= models.BooleanField(default=True)

    def save_average_review(self):
        # Calculate the average review
        average_review = Review.objects.filter(provider=self).aggregate(models.Avg('value'))['value__avg']
        self.average_review = average_review
        self.save()


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
    
    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey (Client, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description= models.TextField()
    post_category = models.ForeignKey (Category, on_delete=models.CASCADE,default="Other")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + "/n" + self.description
    

class Review(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    provider= models.ForeignKey(Provider, on_delete=models.CASCADE)
    value = models.FloatField() 
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['client', 'provider']
        
    def __str__(self):
        return f'{self.user.username} - {self.rating} stars'
    

class Request(models.Model):
    provider= models.ForeignKey(Provider, on_delete=models.CASCADE)
    client= models.ForeignKey(Client, on_delete=models.CASCADE)
    job = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['job', 'provider']

class Accepted(models.Model):
    provider= models.ForeignKey(Provider, on_delete=models.CASCADE)
    client= models.ForeignKey(Client, on_delete=models.CASCADE)
    job = models.ForeignKey(Post, on_delete=models.CASCADE)
    client_done = models.BooleanField (default=False)
    provider_done = models.BooleanField (default=False)
    created_at=models.DateTimeField(auto_now_add=True)

class Done(models.Model):
    provider= models.ForeignKey(Provider, on_delete=models.CASCADE)
    client= models.ForeignKey(Client, on_delete=models.CASCADE)
    job = models.ForeignKey(Post, on_delete=models.CASCADE)

    created_at=models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
    provider= models.ForeignKey(Provider, on_delete=models.CASCADE)
    client= models.ForeignKey(Client, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['client', 'provider']

class Connected(models.Model):
    provider= models.ForeignKey(Provider, on_delete=models.CASCADE)
    client= models.ForeignKey(Client, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['client', 'provider']