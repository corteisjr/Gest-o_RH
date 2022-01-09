from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from  Funcionarios.models import Funcionario

class listFuncionario(ListView):
    model = Funcionario
    
