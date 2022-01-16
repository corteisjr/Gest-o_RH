from django.shortcuts import redirect, render
from django.views.generic import ListView
from departamentos.models import Departamento
from Funcionarios.models import Funcionario

# Listar Departamentos

class listDepartamento(ListView):
    model = Departamento