from dataclasses import fields
from django import forms
from django.forms import ModelForm, inlineformset_factory

from .models import *

class CrearPersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombres', 'apellidos', 'documento', 'telefono']
        labels = {
            'nombres': 'Nombre del rector',
            'apellidos': 'Apellidos del rector',
            'documento': 'Documento del rector',
            'telefono': 'Número de celular'
        }
        widgets = {
            'nombres': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre aqui',
                    'input_type': 'text',
                    'required': True,
                },
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Apellido aqui',
                    'input_type': 'text',
                    'required': True,
                },
            ),
            'documento': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '#',
                    'type': 'number',
                    'required': True,
                }
            ),
            'telefono': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '#',
                    'type': 'number',
                    'required': True,
                }
            ),
        }


class CrearContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ['objeto', 'valor_contrato', 'plazo_ejecucion', 'fecha_inicio', 'fecha_terminacion', 'contratista_id']
        labels = {
            'objeto': 'Objeto del contrato',
            'valor_contrato': 'Valor del contrato',
            'plazo_ejecucion': 'Plazo de ejecución del contrato',
            'fecha_inicio': 'Fecha inicio del contrato',
            'fecha_terminacion': 'Fecha terminación del contrato',
            'contratista_id': 'Nombre del contratista',
        }
        widgets = {
            'objeto': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'objeto',
                    'input_type': 'text',
                    'required': True,
                },
            ),
            'valor_contrato': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '# valor',
                    'type': 'number',
                    'required': True,
                }
            ),
            'plazo_ejecucion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'plazo',
                    'input_type': 'text',
                    'required': True,
                },
            ),
            'fecha_inicio': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'DD/MM/AAAA',
                    'input_type': 'text',
                    'required': True,
                    'id': 'simple-date'
                },
            ),
            'fecha_terminacion': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'DD/MM/AAAA',
                    'input_type': 'text',
                    'required': True,
                    'id': 'simple-date-2'
                },
            ),
            'contratista_id': forms.Select(attrs={'class': 'form-select'})
        }

class CrearEntidadForm(forms.ModelForm):
    class Meta:
        model = Entidad
        fields = ['nombre_entidad', 'nit', 'formato', 'direccion', 'rector_id']
        labels = {
            'nombre_entidad': 'Nombre de entidad',
            'nit': 'Número de identificacion tributaria',
            'formato': 'Formato de cotización para esta entidad',
            'direccion': 'Direccion de entidad',
            'rector_id': 'Rector de entidad'
        }
        widgets = {
            'nombre_entidad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Name',
                    'input_type': 'text',
                    'required': True,
                },
            ),
            'nit': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '# valor',
                    'type': 'number',
                    'required': True,
                }
            ),
            'formato': forms.FileInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Name',
                    'input_type': 'text',
                    'required': True,
                },
            ),
            'rector_id': forms.Select(attrs={'class': 'form-select'})
        }

class ConsultaFormatoForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('contrato_id',)
        labels = {
            'contrato_id': 'Seleccione el contrato del formato'
        }
        widgets = {
            'contrato_id': forms.Select(attrs={'class': 'form-select'})
        }

class EditarContratoForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['numero_item', 'descripcion', 'cantidad', 'unidad_medida']
        labels = {
            'numero_item': 'Numero de item',
            'descripcion': 'Descripcion del item',
            'cantidad': 'Cantidad',
            'unidad_medida': 'Unidad de medida',
        }
        widgets = {
            'numero_item': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '# item',
                    'type': 'number',
                    'required': True,
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Descripcion',
                    'input_type': 'text',
                    'required': True,
                },
            ),
            'cantidad': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Cant',
                    'type': 'number',
                    'required': True,
                }
            ),
            'unidad_medida': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Unidad medida',
                    'input_type': 'text',
                    'required': True,
                },
            ),
        }

FamilyMemberFormSet = inlineformset_factory(Contrato, Item, form=EditarContratoForm, extra=1, fk_name='contrato_id')