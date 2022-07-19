from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

from apps.usuario.models import Usuario
from apps.usuario.forms import *

class Login(FormView):
    template_name = 'inicio/inicio_sesion.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('plantilla_inicio')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = authenticate(username= form.cleaned_data['username'], password= form.cleaned_data['password'])
        if user:
            login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')

class PlantillaInicio(TemplateView):

    template_name = 'inicio/plantilla_inicio.html'

class PlantillaPrincipal(TemplateView):

    template_name = 'inicio/plantilla_principal.html'
