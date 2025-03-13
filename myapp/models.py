from django.db import models

# Create your models here.

class Project (models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 200)
    finished = models.BooleanField(default = False)
    #Creamos la funcion str
    def __str__(self):
        return self.name

class Task (models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 200)
    project = models.ForeignKey(Project, on_delete = models.CASCADE)
    
    #Creamos la funcion str
    def __str__(self):
        return self.title
    
    