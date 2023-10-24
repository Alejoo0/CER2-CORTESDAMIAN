from django.shortcuts               import render
from django.http                    import HttpResponse
from .models                        import Comunicado, Entidad

# Create your views here.

def home(request):
    comunicados = Comunicado.objects.all()
    entidades   = Entidad.objects.all()
    data = {
        'comunicados': comunicados,
        'entidades': entidades
        }
    

    return render(request, 'core/home.html',data)

def filtrar_comunicados(request):
    entidad_id  = request.GET.get('entidad')
    comunicados = Comunicado.objects.all().order_by('-fecha_publicacion')

    if entidad_id:
        comunicados = comunicados.filter(entidad_id=entidad_id)

    entidades = Entidad.objects.all()

    data = {
        'comunicados': comunicados,
        'entidades': entidades
        }

    return render(request, 'core/home.html', data)