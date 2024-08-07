from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        try:
            redirect = self.request.GET['redirect']
            if redirect == 'true':
                return reverse_lazy('mypost')
        except:
            return reverse_lazy('home')