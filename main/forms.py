from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name= forms.CharField(required=True)
    state=forms.CharField(required=True)
    city=forms.CharField(required=True)
    phone=forms.CharField(required=True)
    is_provider=forms.ChoiceField(required=True, widget=forms.RadioSelect, choices={("provider","provider"),("client","client")})
    
    

    class Meta:
        model = User
        fields = ["first_name","last_name","username","email","state","city","phone","password1","password2","is_provider"]



