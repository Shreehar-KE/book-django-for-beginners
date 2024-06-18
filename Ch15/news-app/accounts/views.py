from .forms import CustomerUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


class SignUpView(CreateView):
    form_class = CustomerUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
