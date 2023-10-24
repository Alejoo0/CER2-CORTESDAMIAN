from django.urls import path
from .views      import home,filtrar_comunicados

urlpatterns = [
    path('', home, name="home"),
    path('filtrar_comunicados/', filtrar_comunicados, name='filtrar_comunicados'),
]