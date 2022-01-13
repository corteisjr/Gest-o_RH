from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.urls.base import reverse_lazy
from django.views.generic import ListView, UpdateView
from django.views.generic.edit import DeleteView
from  Funcionarios.models import Funcionario


# Listar
class listFuncionario(ListView):
    model = Funcionario

    # Filtração pela empresa logada
    def get_queryset(self):
        empresa_logada= self.request.user.funcionario.empresas
        queryset= Funcionario.objects.filter(empresas=empresa_logada)
        return queryset

# Actualizar
class updateFuncionario(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']
    
# Deletar

class deleteFuncionario(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')