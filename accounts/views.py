from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
    form_class = CustomUserCreationForm