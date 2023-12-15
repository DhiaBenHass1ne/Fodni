from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from .views import CustomLoginView


urlpatterns = [
    path('',views.home, name= 'home'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('profile',views.profile, name='profile'),
    path('home',views.home, name= 'home'),
    path('accept/<int:request_id>',views.accept_provider, name= 'home'),
    path('reject/<int:request_id>',views.reject_provider, name= 'home'),
    path('accept/c/<int:contact_id>',views.accept_client, name= 'home'),
    path('reject/c/<int:contact_id>',views.reject_client, name= 'home'),
    path('sign-up',views.sign_up, name= 'sign_up'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout_view',views.logout_view, name= 'logout'),
    path('create-post',views.create_post, name= 'post'),
    path('profile',views.profile, name= 'profile'),
    path('profile/edit/<int:id>',views.edit_profile, name= 'edit_profile'),
    path('request/<int:provider_id>/<int:client_id>/<int:post_id>',views.send_request, name= 'request'),
    path('contact/<int:provider_id>/<int:client_id>',views.send_contact, name= 'contact'),
    path('done/p/<int:job_id>',views.provider_done,name='provider_done'),
    path('done/c/<int:job_id>',views.client_done,name='provider_done')

]

