from django.db import models

class ModeloBase(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.BooleanField('Estado', default=True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now_add=True, auto_now=False)
    fecha_modificacion = models.DateField('Fecha de Modificación', auto_now=True, auto_now_add=False)
    fecha_eliminacion = models.DateField('Fecha de Eliminación', auto_now=True, auto_now_add=False)

class Persona(ModeloBase):
    nombres = models.CharField('Nombre de la Persona', max_length=100)
    apellidos = models.CharField('Apellidos de la persona', max_length=100)
    documento = models.IntegerField('Cedula de la persona')
    telefono = models.IntegerField('Numero de celular de la persona', blank=True, null=True)
    direccion = models.CharField('Direccion de la persona', max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'

class Rector(ModeloBase):
    persona_id = models.ForeignKey(Persona, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.persona_id

class Contratista(ModeloBase):
    persona_id = models.ForeignKey(Persona, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.persona_id

class Entidad(ModeloBase):
    nombre_entidad = models.CharField('Nombre de la entidad', max_length=300)
    nit = models.CharField("Numero de identificacion tributaria", max_length=20)
    formato = models.FileField(null=True, blank=True, upload_to='comprobantes/')
    direccion = models.CharField('Direccion Entidad', max_length=50)
    rector_id = models.ForeignKey(Rector, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.nombre_entidad} {self.nit}'

class Contrato(ModeloBase):
    objeto = models.CharField('Objeto del contrato', max_length=100)
    valor_contrato = models.IntegerField('Valor contrato')
    plazo_ejecucion = models.CharField('Plazo ejecutar contrato', max_length=30)
    fecha_inicio = models.DateField('Inicio de contrato')
    fecha_terminacion = models.DateField('Fecha finalizacion contrato')
    vigilancia = models.CharField('Vigilancia contrato', max_length=100,blank=True, null=True)
    entidad_id = models.ForeignKey(Entidad, on_delete=models.CASCADE, blank=True, null=True)
    contratista_id = models.ForeignKey(Contratista, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.entidad_id} {self.objeto}'

class Item(ModeloBase):
    numero_item = models.IntegerField(unique=True)
    descripcion = models.CharField('Descripcion del item', max_length=200)
    cantidad = models.IntegerField('Cantidad del item')
    unidad_medida = models.CharField('Unidad de medida del item', max_length=100)
    contrato_id = models.ForeignKey(Contrato, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.descripcion


