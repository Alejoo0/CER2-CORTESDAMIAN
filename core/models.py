from django.db                  import models
from django.contrib.auth.models import User

TIPO_CHOICES=[
    ("S","Suspensión de actividades"),
    ("C","Suspensión de Clase"),
    ("I","Información")]

class Entidad(models.Model):
    id     = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    logo   = models.ImageField(upload_to="logos", null=True)

    def __str__(self) -> str:
        return self.nombre

class Comunicado(models.Model):
    id                        = models.BigAutoField(primary_key=True)
    titulo                    = models.CharField(max_length=50)
    detalle                   = models.TextField()
    detalle_corto             = models.CharField(max_length=255) 
    tipo                      = models.CharField(max_length=20,choices=TIPO_CHOICES,null=True)
    entidad_id                = models.ForeignKey('Entidad',on_delete=models.CASCADE)
    visible                   = models.BooleanField(default=False)
    fecha_publicacion         = models.DateTimeField(auto_now_add=True)
    fecha_ultima_modificacion = models.DateTimeField(auto_now=True)
    publicado_por             = models.ForeignKey(User, on_delete=models.CASCADE,related_name='comunicados_publicados')
    modificado_por            = models.ForeignKey(User,on_delete=models.CASCADE, related_name='comunicados_modificados')

    def __str__(self) -> str:
        return self.titulo
    
class Administrador(models.Model):
    user    = models.OneToOneField(User, on_delete=models.CASCADE)
    entidad = models.ForeignKey('Entidad', on_delete=models.CASCADE)