from django.db import models
from Funcionarios.models import Funcionario

class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100)
    funcionarios = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.motivo