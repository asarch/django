# Lo que se necesita:

from django.contrib import admin
from django.db.models.base import ModelBase

#from pos import models as pos_models
import models

# Las diferentes versiones:

# notebook/admin.py

#---------------------------------------------------------------------
#  Originalmente el codigo era este:
#---------------------------------------------------------------------

#for name,var in pos_models.__dict__.items():
for name,var in models.__dict__.items():
	if type(var) is ModelBase:
		admin.site.register(var)

#---------------------------------------------------------------------
#  La forma mejorada es este ya que te permite personalizar
#  la forma en que se muestra un modelo (en este caso, las
#  notas del notebook).
#---------------------------------------------------------------------

from django.contrib import admin
from django.db.models.base import ModelBase

#from notebook import models as notebook_models
import models

from models import Nota

# La personalizacion se hace aqui:
class NotaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'descripcion', 'fecha', 'tipo_nota')
	
# Register your models here

#for name,var in notebook_models.__dict__.items():
for name,var in models.__dict__.items():
	if var != Nota:
		if type(var) is ModelBase:
			admin.site.register(var)
			
admin.site.register(Nota, NotaAdmin)

#---------------------------------------------------------------------
#  Para personalizar dos o mas tablas
#---------------------------------------------------------------------

import models

from models import Nota
from models import Cita

class NotaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'descripcion', 'fecha', 'tipo_nota')
	
class CitaAdmin(admin.ModelAdmin):
	list_display = ('texto', 'autor')

lista = ['Nota', 'Cita']

for name,var in models.__dict__.items():
	if name not in lista:
		if type(var) is ModelBase:
			admin.site.register(var)
			
admin.site.register(Nota, NotaAdmin)
admin.site.register(Cita, CitaAdmin)
