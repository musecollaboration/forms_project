from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Gallery


class ListGallery(ListView):
    model = Gallery
    template_name = 'gallery/list_file.html'
    context_object_name = 'records'


class CreateGalleryView(CreateView):
    model = Gallery
    template_name = 'gallery/load_file.html'
    fields = '__all__'
    success_url = 'load_image'
