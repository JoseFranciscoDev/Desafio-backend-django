from django.db import models
from django.contrib.auth.models import AbstractUser

taskChoices = (('pendente', 'Pendente'),('em andamento', 'Em Andamento'), ('concluido', 'Concluido'))

class User(AbstractUser):
    name = models.CharField(max_length=100, default='')
    
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null= True)
    title = models.CharField(max_length=100, default='')
    description = models.TextField(max_length=1000, default='')
    status = models.CharField(max_length=12, default='pendente', choices=taskChoices)
    
# Create your models here.
