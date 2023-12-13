from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Review



class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name= forms.CharField(required=True)
    state=forms.CharField(required=True)
    city=forms.CharField(required=True)
    phone=forms.CharField(required=True)
    is_provider=forms.ChoiceField(required=True, widget=forms.RadioSelect, choices={("Provider","Provider"),("Client","Client")})
    

    class Meta:
        model = User
        fields = ["first_name","last_name","username","email","state","city","phone","password1","password2","is_provider"]



class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["title","description","post_category"]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating']
        widgets = {
            'rating': forms.NumberInput(attrs={'type': 'number', 'step': '0.1', 'min': '0', 'max': '5'}),
        }
