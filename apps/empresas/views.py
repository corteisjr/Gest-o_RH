from django.shortcuts import render
from django.views.generic.edit import CreateView
from empresas.models import Empresa

class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['name']