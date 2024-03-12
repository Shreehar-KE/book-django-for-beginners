from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# from django.contrib.auth import login, authenticate


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    # To automatically login the user after registeration
    # Requires login() & authenticate() methods from "django.contrib.auth"
    # success_url = reverse_lazy('home')

    # def form_valid(self, form):
    #     # Save the user instance
    #     response = super().form_valid(form)
    #     # Log the user in
    #     username = form.cleaned_data['username']
    #     password = form.cleaned_data['password1']
    #     user = authenticate(username=username, password=password)
    #     if user is not None:
    #         login(self.request, user)
    #     return response
