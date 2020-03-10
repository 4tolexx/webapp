from django.shortcuts import render
from .forms import ApplicantForm
from .models import Job
from.import forms
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from allauth.account.views import (LoginView,
                                   LogoutView,
                                   SignupView,
                                   )

# Create your views here


def home(request):
    return render(request, 'tee/home.html')


def about(request):
    return render(request, 'tee/about.html')

def career(request):
    return render(request, 'tee/career.html')

class login(LoginView):
    template_name = 'tee/account/login.html'

class logout(LogoutView):
    template_name = 'tee/account/logout.html'

class signup(SignupView):
    template_name = 'tee/account/signup.html'

class JobDetail(DetailView):
    model = Job
    template_name = 'tee/job_detail.html'


class JobCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Job
    form_class = ApplicantForm
    template_name = 'tee/job_form.html'
    success_message = 'your application has been received, check your mail to see details'

   

class JobUpdate(UpdateView):
    model = Job
    form_class = ApplicantForm
    template_name = 'tee/job_update.html'

