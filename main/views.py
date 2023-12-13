from django.shortcuts import render,redirect, HttpResponse
from .forms import RegisterForm, PostForm,ReviewForm
from .models import Client, Provider,City,User,Review,Category
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

from django.contrib.auth import login, logout, authenticate

class CustomLoginView(LoginView):
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            # If the user is logged in, redirect them to another page
            return redirect('dashboard')  # Replace 'home' with your desired URL name or path
        else:
            return super().dispatch(request, *args, **kwargs)

# Create your views here.
def home(request):
    if request.user.is_authenticated:
            # If the user is logged in, redirect them to another page
        return redirect('dashboard')  # Replace 'home' with your desired URL name or path
    return render(request, 'main/home.html')


def sign_up(request):
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if request.POST["is_provider"]=="Provider":
                created_user = form.save()
                selected_user= User.objects.last()
                Provider.objects.create(user=selected_user, city=City.objects.get(gov=request.POST["city"] ),bio=request.POST["bio"],category=Category.objects.get(title=request.POST["categories"] ) )
                city= request.POST["city"]
                return redirect('/dashboard')
            
            else:
                created_user = form.save()
                selected_user= User.objects.last()
                Client.objects.create(user=selected_user, city=City.objects.get(gov=request.POST["city"] ) )
                city= request.POST["city"]
                bio= request.POST["bio"]
                
        
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

    if len(is_provider)>0 :
        return render(request, 'main/provider_dashboard.html')
    
    if len(is_client)>0 :
        return render(request, 'main/client_dashboard.html')
    
    
    
@login_required
def create_post(request):
    if request.method== 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author= request.user
            post.save()
            return redirect("/home")
    else :
        form = PostForm()
    return render (request, 'main/create_post.html', {"form": form})

@login_required
def profile(request):
    user_id = request.user.id
    is_client=None
    is_provider=None
    is_provider=Provider.objects.filter(user_id=user_id)
    is_client=Client.objects.filter(user_id=user_id)

    if len(is_provider)>0 :
        return render(request, 'main/profile_template_p.html')
    
    if len(is_client)>0 :
        return render(request, 'main/client_dashboard_c.html')
    

# @login_required
# def review_list(request):
#     reviews = Review.objects.all()
#     return render(request, 'reviews/review_list.html', {'reviews': reviews})

# @login_required
# def add_review(request):
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.user = request.user
#             review.provider=
#             review.save()
#             return redirect('review_list')
#     else:
#         form = ReviewForm()

#     return render(request, 'reviews/add_review.html', {'form': form})