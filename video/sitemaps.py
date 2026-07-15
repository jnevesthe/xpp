from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Video, Categoria


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = "daily"

    def items(self):
        return [
            "galeria",
            "search",
            "emphasis",
            "categorias",
        ]

    def location(self, item):
        return reverse(item)


class VideoSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Video.objects.all()

    def lastmod(self, obj):
        return obj.criado_em

    def location(self, obj):
        return reverse("ver_video", args=[obj.slug])


class CategoriaSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Categoria.objects.all()

    def location(self, obj):
        return reverse("videos_categoria", args=[obj.slug])
