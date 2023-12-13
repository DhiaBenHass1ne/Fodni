from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from .views import CustomLoginView


urlpatterns = [
    path('',views.home, name= 'home'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('profile',views.profile, name='profile'),
    path('home',views.home, name= 'home'),
    path('sign-up',views.sign_up, name= 'sign_up'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout_view',views.logout_view, name= 'logout'),
    path('create-post',views.create_post, name= 'post'),
    path('profile',views.profile, name= 'profile'),

]

