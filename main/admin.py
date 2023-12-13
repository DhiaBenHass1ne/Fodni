from django.contrib import admin
from .models import Category, Provider, Client, Post
# Register your models here.
admin.site.register(Category)
admin.site.register(Provider)
admin.site.register(Client)
admin.site.register(Post)