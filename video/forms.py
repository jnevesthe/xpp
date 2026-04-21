from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['titulo', 'descricao', 'video', 'capa', 'categoria']