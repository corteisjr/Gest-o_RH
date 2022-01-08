from django.db import models
from django.shortcuts import redirect
from django.urls import reverse

class Empresa(models.Model):
    name = models.CharField(max_length=100, help_text='Nome da empresa')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')