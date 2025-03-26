from django import forms
from django.contrib.auth.models import User

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo: ",max_length=200)
    description = forms.CharField(label="Descripcion: ",widget=forms.Textarea)
    important = forms.BooleanField(required=False)
    status = forms.CharField(widget=forms.Select(choices=[('Pendiente', 'Pendiente'), ('En proceso', 'En proceso'), ('Terminado', 'Terminado')]))
    userasigned = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))


class CreateNewProject(forms.Form):
    title = forms.CharField(label="Nombre proyecto ",max_length=200)
    description = forms.CharField(label="Descripcion ",widget=forms.Textarea)
    creator = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
