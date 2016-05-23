# In settings.py, after the databases declaration:
#
# DATABASE_ROUTERS = ['projects.router.default']
apps = [
	'agenda',
	'coleccion',
	'imco',
	'jafra',
	'konigin',
	'muebleria',
	'muestra',
	'slackbuild',
]

tables = [
	# Agenda
	'aniversario', 'cita', 'diario', 'enlace',
	'etiqueta', 'expresion_idiomatica', 'idioma',
	'nota', 'nota_etiqueta', 'tarea', 'tipo_aniversario',
	'tipo_nota', 'tipo_tarea',

	# Coleccion
	'archivo', 'blu_ray', 'catalogo', 'contenido',
	'disco', 'respaldo',

	# Imco
	'alumno', 'asistencia', 'evaluacion',

	# Jafra
	'categoria', 'cliente', 'pago', 'producto',
	'venta', 'venta_producto',

	# Konigin
	'evento', 'comentario',

	# Muebleria
	'elemento', 'inventario', 'tipo_elemento'
	
	# Muestra
	'glucosa', 'glucosa_comentario', 'paciente', 'presion',
	
	# Slackbuild
	'archivo', 'listado', 'paquete', 'tipo_archivo',
	'version_slackware'
]

class default(object):
	def db_for_read(self, model, **hints):
		if model._meta.app_label in apps:
			return model._meta.app_label

		return 'default'

	def db_for_write(self, model, **hints):
		if model._meta.app_label in apps:
			return model._meta.app_label

		return 'default'

	def allow_relation(self, obj1, obj2, **hints):
		if obj1._meta.app_label in apps and obj2._meta.app_label in apps:
			return True
		elif [obj1._meta.app_label, obj2._meta.app_label] not in apps:
			return True

		return False

	def allow_migrate(self, db, app_label, model_name=None, **hints):
		if db in tables or model_name in apps:
			return False

		return True
