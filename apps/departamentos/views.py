from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from django.views.generic import ListView, UpdateView
from django.contrib.auth.models import User
from django.views.generic.edit import DeleteView, CreateView
from departamentos.models import Departamento
# Listar Departamentos

class listDepartamento(ListView):
    model = Departamento
    template_name = 'departamento_list.html'
    
    # Filtracao pela empresa logada
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresas
        return Departamento.objects.filter(empresas=empresa_logada)

#Actualizar
class updadeDepartamento(UpdateView):
    model = Departamento
    fields = ['nome']
    
class CreateDepartamento(CreateView):
    model = Departamento
    fields = ['nome']
    
    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresas = self.request.user.funcionario.empresas
        departamento.save()
        return super(CreateDepartamento, self).form_valid(form)
        
#Deletar
class DeleteDepartamento(DeleteView):
    model = Departamento
    success_url = reverse_lazy('list_departamentos')