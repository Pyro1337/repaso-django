from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Project (models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 200)
    datecreated = models.DateTimeField(auto_now_add = True)
    datefinished = models.DateTimeField(null = True)
    finished = models.BooleanField(default = False)
    creator = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
        #Creamos la funcion str
    def __str__(self):
        return self.title
    

class Task (models.Model):
    STATUS_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('En proceso', 'En proceso'),
        ('Terminado', 'Terminado'),
    ]
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 200, blank= True)
    created = models.DateTimeField(auto_now_add = True)
    datefinished = models.DateTimeField(null = True)
    important = models.BooleanField(default = False)
    status = models.CharField(max_length= 20, choices = STATUS_CHOICES, default = 'Pendiente')
    userasigned = models.ForeignKey(User, on_delete = models.CASCADE)
    project = models.ForeignKey(Project, on_delete = models.CASCADE)
    #Creamos la funcion str
    def __str__(self):
        return self.name

    

    