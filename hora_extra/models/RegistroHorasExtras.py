from django.db import models


class RegistroDeHorasExtras(models.Model):
    reason = models.CharField(max_length=100)
    
    
    def __st__(self):
        return self.reason