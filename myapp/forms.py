from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo: ",max_length=200)
    description = forms.CharField(label="Descripcion: ",widget=forms.Textarea)

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre proyecto ",max_length=200)
    description = forms.CharField(label="Descripcion ",widget=forms.Textarea)
