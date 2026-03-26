from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Personaje

def lista_personajes(request):
    personajes_list = Personaje.objects.all()
    paginator = Paginator(personajes_list, 8) # 8 magos por página
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'personajes/lista.html', {'page_obj': page_obj})

def detalle_personaje(request, personaje_id):
    personaje = get_object_or_404(Personaje, id=personaje_id)
    return render(request, 'personajes/detalle.html', {'personaje': personaje})