from django.db import models


class Documento(models.Model):
    description = models.CharField(max_length=100)
    
    
    def __st__(self):
        return self.description