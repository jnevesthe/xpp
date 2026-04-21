
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.galeria, name='galeria'),
    path('video/<slug:slug>/', views.video, name='ver_video'),
    path('search/', views.search, name='search'),
    path('emphasis/', views.destaques, name='emphasis'),
    path('categorias/', views.lista_categorias, name='categorias'),
    path('categoria/<slug:slug>/', views.videos_por_categoria, name='videos_categoria'),
]

# Serve arquivos estáticos e mídia no DEBUG (Termux)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    
