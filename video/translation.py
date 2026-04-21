from modeltranslation.translator import translator, TranslationOptions
from .models import Video, Categoria




class VideoTranslationOptions(TranslationOptions):
    fields = ('titulo', 'descricao', 'slug')

translator.register(Video, VideoTranslationOptions)



class CategoriaTranslationOptions(TranslationOptions):
    fields = ('nome', 'slug')

translator.register(Categoria, CategoriaTranslationOptions)

