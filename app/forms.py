from django import forms
from app.models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        # fields = ('title', 'description', 'thumb', 'slug')
        exclude = []

    zip = forms.FileField(required=False)