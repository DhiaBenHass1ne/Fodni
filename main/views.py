from django.shortcuts import render,redirect, HttpResponse
from .forms import RegisterForm
from .models import Client, Provider,City,User
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, logout, authenticate


# Create your views here.
@login_required
def home(request):
    return render(request, 'main/home.html')

def sign_up(request):
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if request.POST["is_provider"]=="provider":
                created_user = form.save()
                selected_user= User.objects.last()
                Provider.objects.create(user=selected_user, city=City.objects.get(gov=request.POST["city"] ) )
                city= request.POST["city"]
                return redirect('/login')
            
            else:
                created_user = form.save()
                selected_user= User.objects.last()
                Client.objects.create(user=selected_user, city=City.objects.get(gov=request.POST["city"] ) )
                city= request.POST["city"]
                
        
                return redirect('/login')
                
    else:
        form = RegisterForm()
    return render (request,'registration/sign_up.html',{"form": form})

@login_required
def logout_view(request):
    logout(request)
    return HttpResponse("Logged Out")

