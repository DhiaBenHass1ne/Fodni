from django.shortcuts import render,redirect, HttpResponse
from .forms import RegisterForm
from .models import Client, Provider,City,User
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, logout, authenticate


# Create your views here.
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
                return redirect('/dashboard')
            
            else:
                created_user = form.save()
                selected_user= User.objects.last()
                Client.objects.create(user=selected_user, city=City.objects.get(gov=request.POST["city"] ) )
                city= request.POST["city"]
                
        
                return redirect('/dashboard')
                
    else:
        form = RegisterForm()
    return render (request,'registration/sign_up.html',{"form": form})



@login_required
def logout_view(request):
    logout(request)
    return redirect('/home')

@login_required
def profile(request):
    #logic here
    return render(request,"main/profile_template.html")




@login_required
def dashboard(request):
    user_id = request.user.id
    is_client=None
    is_provider=None
    is_provider=Provider.objects.filter(user_id=user_id)
    is_client=Client.objects.filter(user_id=user_id)
    print("xxxxxxxxxxxxxxxxxxxxxxxxxx",is_client)
    print("xxxxxxxxxxxxxxxxxxxxxxxxxx",is_provider)

    if len(is_provider)>0 :
        return render(request, 'main/provider_dashboard.html')
    
    if len(is_client)>0 :
        return render(request, 'main/client_dashboard.html')
    
    
    
