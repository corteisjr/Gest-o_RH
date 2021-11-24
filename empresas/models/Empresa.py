from django.db import models


class Empresa(models.Model):
    name = models.CharField(max_length=100, help_text="Nome da empresa")
    
    
    def __st__(self):
        return self.name