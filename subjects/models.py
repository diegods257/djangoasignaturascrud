from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Registros(models.Model):
  id = models.AutoField(primary_key=True)
  programa = models.CharField(max_length=30)
  materia = models.CharField(max_length=30)
  creditos = models.CharField(max_length=30)
  fechamatricula = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE) 

  def __str__(self):
    texto = "{0} {1}"
    return texto.format(self.programa, self.materia)
  
