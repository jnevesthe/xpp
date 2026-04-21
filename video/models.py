from django.db import models
from django.utils.text import slugify
from django.utils.translation import get_language
from cloudinary.models import CloudinaryField


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)       # independente, sempre PT
 
    def save(self, *args, **kwargs):
        # Slug independente sempre em português
        if not self.slug:
            self.slug = slugify(self.nome)

        # Slug português
        if not self.slug_pt:
            self.slug_pt = slugify(self.nome)

        # Slug inglês
        if not self.slug_en:
            nome_en = getattr(self, 'nome_en', None) or self.nome
            self.slug_en = slugify(nome_en)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome


class Video(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    video = CloudinaryField('video', resource_type='video')
    capa = CloudinaryField('image')
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    destaque = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)       # independente, sempre PT
    

    def save(self, *args, **kwargs):
        # Slug independente sempre em português
        if not self.slug:
            self.slug = slugify(self.titulo)

        # Slug português
        if not self.slug_pt:
            self.slug_pt = slugify(self.titulo)

        # Slug inglês
        if not self.slug_en:
            titulo_en = getattr(self, 'titulo_en', None) or self.titulo
            self.slug_en = slugify(titulo_en)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo


class TrafficLog(models.Model):
    ip = models.GenericIPAddressField()
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    path = models.CharField(max_length=200)
    user_agent = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return f"{self.ip} - {self.path} - {self.date}"
