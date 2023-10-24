from django.contrib                     import admin
from .models                            import Entidad, Comunicado, Administrador

admin.site.register(Entidad)
admin.site.register(Comunicado)
admin.site.register(Administrador)
