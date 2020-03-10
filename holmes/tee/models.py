# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from .choices import (roles, subjects, EDUCATION_CHOICES, GENDER_CHOICES)
from django.urls import reverse



class Job(models.Model):
    full_name = models.CharField(max_length=30)
    gender = models.CharField(choices=GENDER_CHOICES, max_length = 10)
    address = models.CharField(max_length=30)
    phone_no = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    photo = models.ImageField(upload_to='employer/%Y/%m/%d', blank=True)
    education = models.CharField( 
            max_length=25, 
            blank=True, 
            choices=EDUCATION_CHOICES, 
        )    
    subjects = models.CharField(choices=subjects, max_length=30)
    position = models.CharField(choices=roles, max_length=30)
    resume = models.FileField(upload_to = 'documents')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


    def get_absolute_url(self):
        return reverse('tee:job-detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.full_name
 