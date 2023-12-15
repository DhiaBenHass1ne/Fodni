from django.shortcuts import render,redirect, HttpResponse
from .forms import RegisterForm, PostForm,ReviewForm,EditForm
from .models import Client, Provider,City,User,Review,Category,Post,Request,Contact,Accepted,Connected,Done
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
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            if request.POST["is_provider"]=="Provider":
                created_user = form.save()
                selected_user= User.objects.last()
                Provider.objects.create(user=selected_user, city=City.objects.get(gov=request.POST["city"] ),bio=request.POST["bio"],category=Category.objects.get(title=request.POST["categories"] ), phone=request.POST["phone"], image=request.FILES["image"] )
                city= request.POST["city"]
                return redirect('/dashboard')
            
            else:
                created_user = form.save()
                selected_user= User.objects.last()
                Client.objects.create(user=selected_user, city=City.objects.get(gov=request.POST["city"] ), phone=request.POST["phone"], image=request.FILES["image"] )
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
        posts=[]
        request_id=[]
        provider=is_provider[0]
        all_contacts=Contact.objects.filter(provider_id=provider.id)
        count_con=all_contacts.count()
        requests=Request.objects.all()
        all_accepted=Accepted.objects.filter(provider_id=provider.id)
        
        
        for one_request in requests:
            request_id.append(one_request.job_id)
        all_posts=Post.objects.all()
        for post in all_posts:
            if post.author.city.gov == is_provider[0].city.gov and post.post_category.id == is_provider[0].category.id and post.id not in request_id :
                posts.append(post)
        context={"posts":posts,"provider":provider, "requests":requests, "all_contacts":all_contacts,"count_contacts":count_con, "all_accepted":all_accepted}
        return render(request, 'main/provider_dashboard.html', context=context)
    
    if len(is_client)>0 :
        categories=Category.objects.all()
        providers=Provider.objects.all()
        client=is_client[0]
        all_requests=Request.objects.filter(client_id=client.id)
        count_req=all_requests.count()
        posts=Post.objects.filter(author_id=client.id)
        accepted_posts=Accepted.objects.filter(client_id=client.id)
        accepted_id=[]
        for one_accepted in accepted_posts:
            accepted_id.append(one_accepted.job.id)
        if request.method== 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author= client
                post.save()
                return redirect("/dashboard")
        else :
            form = PostForm()
        context={"client":client, "categories":categories, "providers":providers, "form":form, "posts":posts,"requests":all_requests,"count_req":count_req, "accepted_posts":accepted_posts,"accepted_ids":accepted_id}
        return render(request, 'main/client_dashboard.html', context=context)
    
    
    
@login_required
def create_post(request):
    if request.method== 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author= request.user
            post.save()
            return redirect("/client_dashboard")
    else :
        form = PostForm()
    return render (request, 'main/client_dashboard.html', {"form": form})

@login_required
def profile(request):
    user_id=request.user
    is_client=None
    is_provider=None
    is_provider=Provider.objects.filter(user_id=user_id)
    is_client=Client.objects.filter(user_id=user_id)


    if len(is_provider)>0 :
        context={"provider":is_provider[0]}
        return render(request, 'main/provider_profile.html',context=context)
    
    if len(is_client)>0 :
        context={"client":is_client[0]}
        return render(request, 'main/client_profile.html',context=context)

@login_required
def edit_profile(request, id):
    user_id = id
    is_provider = Provider.objects.filter(user_id=user_id)
    is_client = Client.objects.filter(user_id=user_id)
    curr_user=User.objects.filter(id=user_id)
    if len(is_provider) > 0:
        form = EditForm(request.POST, request.FILES)
        if request.method == 'POST' and form.is_valid():
            p = Provider.objects.get(user_id=user_id)
            u = User.objects.get (id=user_id)
            u.first_name = request.POST["first_name"]
            u.last_name = request.POST["last_name"]
            p.city = City.objects.get(gov=request.POST["city"])
            p.bio = request.POST["bio"]
            p.category = Category.objects.get(title=request.POST["categories"])
            p.phone = request.POST["phone"]
            u.email = request.POST["email"]
            p.image = request.FILES["image"]

            p.save()
            u.save()
            return redirect("/profile")
        else:
            form=EditForm()
            context = {"provider": is_provider[0], "form": form}
            return render(request, 'main/provider_profile_edit.html', context=context)

    elif len(is_client) > 0:
        instance={"first_name":curr_user[0].first_name, "last_name":curr_user[0].last_name, "city":is_client[0].city, "phone":is_client[0].phone, "email":curr_user[0].email
        
    }
        form = EditForm(request.POST, request.FILES)
        if request.method == 'POST' and form.is_valid():
            c = Client.objects.get(user_id=user_id)
            u = User.objects.get(id=user_id)
            u.first_name = request.POST["first_name"]
            u.last_name = request.POST["last_name"]
            c.city = City.objects.get(gov=request.POST["city"])
            c.phone = request.POST["phone"]
            u.email = request.POST["email"]
            c.image = request.FILES["image"]

            c.save()
            u.save()
            return redirect("/profile")
        else:
            form = EditForm()
            context = {"client": is_client[0], "form": form}
            return render(request, 'main/client_profile_edit.html', context=context)    

@login_required
def send_request(request, provider_id,client_id,post_id):
    curr_provider=Provider.objects.get(id=provider_id)
    curr_client=Client.objects.get(id=client_id)
    curr_post=Post.objects.get(id=post_id)
    Request.objects.create(provider=curr_provider, client=curr_client,job = curr_post)
    return redirect ("/dashboard")

@login_required
def send_contact(request, provider_id,client_id):
    curr_provider=Provider.objects.get(id=provider_id)
    curr_client=Client.objects.get(id=client_id)
    Contact.objects.create(provider=curr_provider, client=curr_client)
    return redirect ("/dashboard")


@login_required
def accept_provider(request,request_id):
    curr_request= Request.objects.get(id=request_id)
    Accepted.objects.create(client_id=curr_request.client.id, provider_id=curr_request.provider.id, job_id=curr_request.job.id)
    curr_request.delete()
    return redirect("/dashboard")


@login_required
def reject_provider(request,request_id):
    curr_request=Request.objects.get(id=request_id)
    curr_request.delete()
    return redirect('/dashboard')

@login_required
def accept_client(request,contact_id):
    curr_contact= Contact.objects.get(id=contact_id)
    Connected.objects.create(client_id=curr_contact.client.id, provider_id=curr_contact.provider.id)
    curr_contact.delete()
    return redirect("/dashboard")


@login_required
def reject_client(request,contact_id):
    curr_contact=Contact.objects.get(id=contact_id)
    curr_contact.delete()
    return redirect('/dashboard')

@login_required
def provider_done(request,job_id):
    curr_job=Accepted.objects.get(job_id=job_id)
    if curr_job.client_done==True:
        Done.objects.create(job_id=job_id,provider_id=curr_job.provider.id, client_id=curr_job.client.id)
        curr_job.delete()
    else :
        curr_job.provider_done=True
        curr_job.save()
    return redirect('/dashboard')

@login_required
def client_done(request,job_id):
    curr_job=Accepted.objects.get(job_id=job_id)
    if curr_job.provider_done==True:
        Done.objects.create(job_id=job_id,provider_id=curr_job.provider.id, client_id=curr_job.client.id)
        curr_job.delete()
    else :
        curr_job.client_done=True
        curr_job.save()
    return redirect('/dashboard')
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