from statistics import mode
from django.db import transaction
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, View
from django.http import HttpResponse, JsonResponse

from .models import *
from .forms import *

# Create your views here.

class Error404(TemplateView):

    template_name = 'error/error_404.html'

class ListaEntidades(TemplateView):

    template_name = 'entidad/lista_entidades.html'

    def get_context_data(self, **kwargs):
        context = {}
        context['entidades'] = Entidad.objects.all().values_list('id', 'nombre_entidad', 'nit', 'direccion', 'rector_id')
        return context
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

class ListaContratos(TemplateView):

    template_name = 'contrato/lista_contratos.html'

    def get_context_data(self, **kwargs):
        context = {}
        context['contratos'] = Contrato.objects.all().values_list('id', 'entidad_id', 'valor_contrato', 'plazo_ejecucion', 'objeto')
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

class ListaRectores(TemplateView):

    template_name = 'persona/lista_rectores.html'

    def get_context_data(self, **kwargs):
        context = {}
        personas_id = Rector.objects.all().values_list('id', flat=True)
        rectores = []
        if personas_id:
            for persona in personas_id:
                rector = Persona.objects.filter(id=persona).values_list('nombres', 'apellidos', 'documento', 'telefono').first()
                if rector:
                    rectores.append(rector)
        context['rectores'] = rectores
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

class ListaContratistas(TemplateView):

    template_name = 'persona/lista_contratistas.html'

    def get_context_data(self, **kwargs):
        context = {}
        personas_id = Contratista.objects.all().values_list('id', flat=True)
        contratistas = []
        for persona in personas_id:
            contratista = Persona.objects.filter(id=persona).values_list('nombres', 'apellidos', 'documento', 'telefono').first()
            if contratista:
                contratistas.append(contratista)
        context['contratistas'] = contratistas
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

class CrearRector(CreateView):
    model = Persona
    form_class = CrearPersonaForm
    template_name = 'persona/crear_rector.html'

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST)
            if form.is_valid():
                persona = form.save()
                Rector.objects.create(
                    persona_id = persona.id
                )
                mensaje = 'Se ha creado exitosamente al rector!'
                error = 'No hay errores'
                response = JsonResponse({'mensaje':mensaje,'error':error, 'url': f'/persona/listado_personas/'})
                response.status_code = 201
                return response
            else:
                mensaje = 'No se ha podido crear la persona correctamente.'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('entidades:error_404')

class CrearContratista(CreateView):
    model = Persona
    form_class = CrearPersonaForm
    template_name = 'persona/crear_contratista.html'

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST)
            if form.is_valid():
                persona = form.save()
                Rector.objects.create(
                    persona_id = persona.id
                )
                mensaje = 'Se ha creado exitosamente al contratista!'
                error = 'No hay errores'
                response = JsonResponse({'mensaje':mensaje,'error':error, 'url': f'/persona/listado_personas/'})
                response.status_code = 201
                return response
            else:
                mensaje = 'No se ha podido crear la persona correctamente.'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('entidades:error_404')

class CrearEntidad(CreateView):
    model = Entidad
    form_class = CrearEntidadForm
    template_name = 'entidad/crear_entidad.html'

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                mensaje = 'Se ha creado exitosamente la entidad!'
                error = 'No hay errores'
                response = JsonResponse({'mensaje':mensaje,'error':error, 'url': f'/entidad/listado_entidades/'})
                response.status_code = 201
                return response
            else:
                mensaje = 'No se ha podido crear la entidad correctamente.'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('entidades:error_404')

class CrearContrato(CreateView):
    model = Entidad
    form_class = CrearContratoForm
    template_name = 'contrato/crear_contrato.html'

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                mensaje = 'Se ha creado exitosamente el contrato!'
                error = 'No hay errores'
                response = JsonResponse({'mensaje':mensaje,'error':error, 'url': f'/contrato/listado_contratos/'})
                response.status_code = 201
                return response
            else:
                mensaje = 'No se ha podido crear el contrato correctamente.'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('entidades:error_404')

class ConsultaContrato(View):

    model = Item
    form_class = ConsultaFormatoForm
    template_name = 'contrato/consulta_contrato.html'

    def get_context_data(self, **kwargs):
        context = {}
        context['form'] = self.form_class
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST)
            if form.is_valid():
                contrato_id = form.cleaned_data.get('contrato_id')
                mensaje = 'Se ha realizado exitosamente la consulta!'
                error = 'No hay errores'
                response = JsonResponse({'mensaje':mensaje,'error':error, 'url': f'/entidades/editar_formato_contrato/{contrato_id.id}'})
                response.status_code = 201
                return response
            else:
                mensaje = 'No se ha podido realizar la consulta.'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('entidades:error_404')

class EditarFormatoContrato(CreateView):
    model = Item
    fields = ['numero_item', 'descripcion', 'cantidad', 'unidad_medida']
    template_name = 'contrato/editar_formato_contrato.html'

    def get_context_data(self, **kwargs):
        context = super(EditarFormatoContrato, self).get_context_data(**kwargs)
        if self.request.POST:
            context['itemform'] = EditarContratoForm(self.request.POST)
        else:
            context['itemform'] = EditarContratoForm()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        items = context['itemform']
        with transaction.atomic():
            self.object = form.save()

            if items.is_valid():
                items.instance = self.object
                items.save()
        return super(EditarFormatoContrato, self).form_valid(form)


