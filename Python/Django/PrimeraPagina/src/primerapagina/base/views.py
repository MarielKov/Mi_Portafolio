from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import Tarea
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.urls import reverse_lazy
# Create your views here.


class logIn(LoginView):
    template_name = "base\login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tareas')

class registro(FormView):
    template_name = 'base/registro.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("tareas")

    def form_valid(self, form):
        usuario = form.save()
        if usuario is not None:
            logIn(self.request, usuario)
        return super(registro, self).form_valid()

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tareas')
        return super(registro, self).get(*args, **kwargs)

class listaPendientes(LoginRequiredMixin,ListView):
    model = Tarea
    context_object_name = "tareas"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tareas'] = context['tareas'].filter(usuario = self.request.user)
        context['count'] = context['tareas'].filter(completo=False).count()

        buscarValor = self.request.GET.get('buscar') or ''

        if buscarValor:
            context['tareas'] = context['tareas'].filter(titulo__icontains=buscarValor)
        context['buscarValor'] = buscarValor
        return context

class detalleTarea(LoginRequiredMixin,DetailView):

    model = Tarea
    context_object_name = "tarea"
    template_name = "base/tarea.html"

class crearTareas(LoginRequiredMixin,CreateView):
    model = Tarea
    fields = ['titulo','descripcion', 'completo']
    success_url = reverse_lazy("tareas")
    def form_valid(self, form):
        form.instance.usuario = self.request.user

        return super(crearTareas, self).form_valid(form)


class editarTarea(LoginRequiredMixin,UpdateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'completo']
    success_url = reverse_lazy("tareas")

class eliminarTarea(LoginRequiredMixin,DeleteView):
    model = Tarea
    context_object_name = "tarea"
    success_url = reverse_lazy("tareas")

