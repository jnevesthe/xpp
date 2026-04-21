# video/admin.py
from django.contrib import admin
from .models import Video, Categoria

# Não usamos mais TranslationAdmin, apenas registro normal
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'destaque', 'criado_em')
    search_fields = ('titulo', 'descricao')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug')
    search_fields = ('nome',)
