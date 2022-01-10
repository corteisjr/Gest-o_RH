from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView
from  Funcionarios.models import Funcionario

class listFuncionario(ListView):
    model = Funcionario
