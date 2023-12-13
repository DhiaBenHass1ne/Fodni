from django.shortcuts import redirect
from django.urls import reverse
from .models import User

class RedirectLoggedInUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.path == reverse('login'):  # Assuming your login URL name is 'login'
            return redirect('dashboard')  # Redirect to a different page after login, change 'dashboard' to your desired URL name
        return self.get_response(request)
