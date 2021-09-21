from django.db import models
from django.db.models.base import Model

# Create your models here.

class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='searches'
    
    def __str__(self) -> str:
        return self.search