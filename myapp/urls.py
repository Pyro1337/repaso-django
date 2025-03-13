from django.urls import path #importamos path de django
from myapp.views  import initial_salute,about,specific_salute,specific_project,projects,specific_task,tasks,create_task,create_project #importamos los views de este modulo


#Creamos y colocamos las rutas aqui
urlpatterns = [
    path('',initial_salute),
    path('about/',about),
    path('<str:username>',specific_salute),
    path('projects/',projects),
    path('projects/<int:id>',specific_project),
    path('tasks/',tasks),
    path('tasks/<int:id>',specific_task),
    path('create_task/',create_task),
    path('create_project/',create_project)

]