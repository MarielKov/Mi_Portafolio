from django.urls import path
from .views import listaPendientes, detalleTarea, crearTareas, editarTarea, eliminarTarea, logIn, registro
from django.contrib.auth.views import LogoutView
urlpatterns =[path("",listaPendientes.as_view(), name="tareas"),
              path("login/",logIn.as_view(), name="login"),
              path("logout/",LogoutView.as_view(next_page = 'login'), name="logout"),
              path("tarea/<int:pk>",detalleTarea.as_view(), name="tarea"),
              path("crear-tarea/",crearTareas.as_view(), name="crear-tarea"),
              path("editar-tarea/<int:pk>",editarTarea.as_view(), name="editar-tarea"),
              path("eliminar-tarea/<int:pk>",eliminarTarea.as_view(), name="eliminar-tarea"),
              path("registrar/",registro.as_view(), name="registrar")]
