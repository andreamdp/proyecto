# -*- encoding: utf-8 -*-
from django.forms.models import fields_for_model
from django.contrib import admin
from pruebas.models import *
from django.forms import TextInput, Textarea
#from grappelli.actions import csv_export_selected
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from pruebas.forms import *


class PresupuestoOptions(admin.ModelAdmin):
    list_display = ('obra','cliente','monto_obra')
    list_filter = ('cliente__ciudad',)
    list_display_links = list_display
#    search_fields = ('nombre', 'apellido', 'cliente_nro','cuit')
#    readonly_fields = ('monto_obra',)
   # formfield_overrides = {
   #     models.TextField: {'widget': MarkItUpWidget},
   # }
    readonly_fields = ('totalHormigon')
    
    form = PresuForm
    fieldsets = (
        (None,{
            'fields':(('cliente','obra',),)}),
        
        ('Estructura Hormigón', {
	        'classes' : ('collapse closed',),            
                'classes' : ('grp-collapse grp-open',),
                'fields':(('totalHormigon'),('bases','vigas_fundacion','columnas'),('vigas_encadenado','piso'),)}),
        ('Estructura Metálica', { 
            'classes' : ('collapse closed',),
            'fields':(('platinas','columnas_principales','columnas_mojinete','arcos_vigas'),('buloneria','tensores','metalica_otros'),)
            }),
        ('Cerramientos', { 
            'classes' : ('collapse closed',),
            'fields':(('mamposteria','correas_cerramiento','fieltro_aislante_cerramiento','chapa_cerramiento'),('buloneria_cerramiento',                     'zingueria_cerramiento','otros_cerramiento'),)
            }),
        ('Cubierta Metálica', { 
            'classes' : ('collapse closed',),
            'fields':(('correas','fieltro_aislante','chapa','canaletas'),('zingueria','cubierta_otros'),)
            }),
        ('Entrepiso', { 
            'classes' : ('collapse closed',),
            'fields':(('hormigon','metalico'),)
            }),
        ('Instalaciones', { 
            'classes' : ('collapse closed',),
            'fields':(('sanitaria','gas','agua','pluviales'),('electrica','aire_calefaccion','instalaciones_otros'),)
            }),
        ('Varios', { 
            'classes' : ('collapse closed',),
            'fields':(('contrapisos','carpetas','revoques','pisos_revestimientos'),('cielorrasos','carpinteria','pintura','herreria'),)
            }),
        ('Subtotales', { 
            'classes' : ('collapse closed',),
            'fields':(('monto_obra', 'monto_general', 'monto_estructura_hormigon', 'monto_estructura_metalica'),('monto_cerramiento', 'monto_cubierta_metalica','monto_instalaciones','monto_varios'),)
            }),


    )




admin.site.register(Presupuesto)


