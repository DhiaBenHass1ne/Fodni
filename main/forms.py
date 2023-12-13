from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Review, Category



class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name= forms.CharField(required=True)
    state=forms.CharField(required=True)
    city=forms.CharField(required=True)
    phone=forms.CharField(required=True)
    is_provider=forms.ChoiceField(required=True, widget=forms.RadioSelect, choices={("Provider","Provider"),("Client","Client")})
    bio = forms.CharField(required=False)
    categories = forms.ChoiceField(required=False, choices=[])
    image = forms.ImageField()
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['categories'].choices = self.get_categories()

    
    def get_categories(self):
        return [(category.title, category.title) for category in Category.objects.all()]

    class Meta:
        model = User
        fields = ["image","first_name","last_name","username","email","state","city","phone","password1","password2","is_provider","bio","categories"]

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
