from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Categoria, Video

# Galeria: mostra 10 miniaturas por página
def galeria(request):
    todos_videos = Video.objects.all().order_by('-criado_em')
    paginator = Paginator(todos_videos, 10)  # 10 vídeos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'galeria.html', {'page_obj': page_obj})

# Página individual do vídeo
def video(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'ver_video.html', {'video': video})


from django.db.models import Q
import random



from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render, redirect




from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

def search(request):
    query = request.GET.get('q', '').strip()
    if not query:
        return redirect('galeria')  # redireciona se pesquisa vazia

    palavras = query.split()

    # Busca categorias
    q_categorias = Q()
    for p in palavras:
        q_categorias |= Q(nome__icontains=p)
    categorias_result = Categoria.objects.filter(q_categorias)

    # Busca vídeos
    q_videos = Q()
    for p in palavras:
        q_videos |= Q(titulo__icontains=p)
    videos_result = Video.objects.filter(q_videos).distinct()

    # Se não encontrar resultados, pega vídeos aleatórios
    if not categorias_result.exists() and not videos_result.exists():
        videos_result = Video.objects.order_by('?')

    # Paginação de 10 vídeos por página
    paginator = Paginator(videos_result, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'query': query,
        'categorias': categorias_result,
        'page_obj': page_obj,
    }

    return render(request, 'search_results.html', context)


def destaques(request):
    # Pega todos os vídeos com destaque = True, mais recentes primeiro
    videos = Video.objects.filter(destaque=True).order_by('-criado_em')

    # Paginação: 10 vídeos por página
    paginator = Paginator(videos, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }
    return render(request, 'destaques.html', context)





def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias.html', {
        'categorias': categorias
    })


def videos_por_categoria(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    videos_list = Video.objects.filter(categoria=categoria).order_by('-criado_em')

    paginator = Paginator(videos_list, 10)  # sempre 10
    page_number = request.GET.get('page')
    videos = paginator.get_page(page_number)

    return render(request, 'videos_categoria.html', {
        'categoria': categoria,
        'videos': videos
    })
