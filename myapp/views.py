from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Project, Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Importamos el modelo de usuario
from .forms import CreateNewTask, CreateNewProject  # importamos el formulario
from django.db import IntegrityError #Para manejar los errores de integridad con respecto al usuario
from django.contrib.auth import login, logout, authenticate # para manejar el login de los usuarios con su respectiva clave o cookie
from django.contrib.auth.forms import AuthenticationForm #importamos la autenticacion del usuario.


# Create your views here.


def signup(request):
    if request.method == 'GET':
        return render(request, "signup.html", {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                #una vez guardamos el usuario lo logeamos
                login(request,user)
                return redirect('/landing_page/') #redigirimos a la pagina principal
            except IntegrityError:
                return render(request, "signup.html", {
                    'form': UserCreationForm,
                    'error': "El usuario ya existe"
                })
                
        return render(request, "signup.html", {
            'form': UserCreationForm,
            'error': "Las contraseñas no coinciden"
        })


def landing_page(request):
    return render(request, "index.html")


def signout(request):
    logout(request)
    response = redirect('/signin')
    response.delete_cookie('sessionid')
    return response

def signin(request):
    if request.method == 'GET':
        return render(request, "signin.html", {
            'form': AuthenticationForm
        })
    else:
       user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
       if user is None:
            return render(request, "signin.html",{
           'form': AuthenticationForm,
           'error': "El usuario o la contraseña son incorrectos"
            })
       else:
           login(request, user)
           return redirect('/landing_page/')




#def specific_salute(request, username):
   # return HttpResponse("<h2>Hello Sr. %s" % username)


def about(request):
    autor_pagina = 'Ivan Sanchez'
    return render(request, "about.html", {'autor_pagina': autor_pagina})


def specific_project(request, id):
    projects = get_object_or_404(Project, id=id)
    return HttpResponse("<h2>Nombre del proyecto: %s</h2>" % projects.title)


def projects(request):
    # projects = list(Project.objects.values())
    # return JsonResponse(projects, safe = False)
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects
    })


def specific_task(request, id):
    tasks = get_object_or_404(Task, id=id)
    return HttpResponse("<h3>Nombre de la tarea: %s </h3>" % tasks.title)


def tasks(request):
    # tasks = list(Task.objects.values())
    # return JsonResponse(tasks, safe = False)
    projects = Project.objects.all()
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'projects': projects,
        'tasks': tasks
    })

# declaramos el formulario


def create_task(request):
    projects = Project.objects.all()  # ✅ Obtener todos los proyectos correctamente

    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'projects': projects,
            'form': CreateNewTask()
        })
    else:
        form = CreateNewTask(request.POST)
        if form.is_valid():
            # ✅ Obtener el proyecto correcto
            project = get_object_or_404(Project, id=request.POST['project'])
            Task.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                important = form.cleaned_data['important'],
                status = form.cleaned_data['status'],
                userasigned = form.cleaned_data['userasigned'],
                project=project
                
            )
            return redirect('/tasks/')
        else:
            return render(request, 'create_task.html', {
                'form': form,
                'projects': projects,  # ✅ Asegurar que los proyectos se envían
                'error': 'Formulario inválido'
            })


def create_project(request):
    if request.method == 'GET':
        return render(request, 'create_project.html', {
            'form': CreateNewProject()
        })
    else:
        form = CreateNewProject(request.POST)
        if form.is_valid():
            Project.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                creator = form.cleaned_data['creator']
            )
            return redirect('/projects/')
        else:
            return render(request, 'create_project.html', {
                'form': form,
                'error': 'Formulario inválido'
            })
