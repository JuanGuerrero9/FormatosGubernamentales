from unicodedata import name
from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    path('crear_entidad/', login_required(CrearEntidad.as_view()), name='crear_entidad'),
    path('lista_entidades/', login_required(ListaEntidades.as_view()), name='lista_entidades'),

    path('crear_contrato/', login_required(CrearContrato.as_view()), name='crear_contrato'),
    path('lista_contratos/', login_required(ListaContratos.as_view()), name='lista_contratos'),

    path('crear_rector/', login_required(CrearRector.as_view()), name='crear_rector'),
    path('lista_rectores/', login_required(ListaRectores.as_view()), name='lista_rectores'),
    
    path('crear_contratista/', login_required(CrearContratista.as_view()), name='crear_contratista'),
    path('lista_contratistas/', login_required(ListaContratistas.as_view()), name='lista_contratistas'),

    path('consulta_contrato/', login_required(ConsultaContrato.as_view()), name='consulta_contrato'),
    path('editar_formato_contrato/<int:contrato>/', login_required(EditarFormatoContrato.as_view()), name='editar_formato_contrato'),


    path('error_404/', login_required(Error404.as_view()), name='error_404'),

]