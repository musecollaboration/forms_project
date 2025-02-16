from django import forms


class GalleryUploadForm(forms.Form):
    image = forms.FileField()
