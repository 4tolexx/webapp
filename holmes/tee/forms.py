from django import forms
from .models import Job
from django.forms import ModelForm, Textarea


class ApplicantForm(ModelForm):  
    class Meta:
        model = Job 
        exclude = ['created_by',]
       