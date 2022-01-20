from django.shortcuts import render
from django.urls import reverse
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .models import Documento

class DocumentCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.pertence_id = self.kwargs['funcionario_id'] 
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)