from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .models import Documento

class DocumentCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.funcionario_id = self.kwargs['funcionarios_id']
        
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)