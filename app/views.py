from django.shortcuts import render
from django.http import HttpRequest
from django.utils.crypto import get_random_string
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView

from app.models import Album, AlbumImage

def home(request):
    print(request)
    return render(request, "home.html", {'user': request.user})

def gallery(request):
    list = Album.objects.filter(is_visible=True).order_by('-created')
    paginator = Paginator(list, 10)

    #Test to generate solid hash password
    hash_phrase = get_random_string(length=18, allowed_chars='_0987654321&#$ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba')
    print(hash_phrase)

    page = request.GET.get('page')
    try:
        albums = paginator.page(page)
    except PageNotAnInteger:
        albums = paginator.page(1) #Si página no es entero, mostrar la primara.
    except EmptyPage:
        albums = paginator.page(paginator.num_pages) #Si página esta fuera de rango, mostrar la ultima.

    return render(request, 'gallery.html', { 'albums': list })

class AlbumDetail(DetailView):
     model = Album

     def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AlbumDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the images
        context['images'] = AlbumImage.objects.filter(album=self.object.id)
        return context

def handler404(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'handler404.html', None, None, 404)