from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from empresas.models import Empresa

class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['name']
    
    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresas = obj
        funcionario.save()
        return HttpResponse('Ok')