from django.urls import path
from .views import lista_personajes, detalle_personaje

urlpatterns = [
    path('', lista_personajes, name='lista_personajes'),
    path('personaje/<int:personaje_id>/', detalle_personaje, name='detalle_personaje'),
]