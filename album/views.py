from django.shortcuts import render

from .models import Album

# Create your views here.
 
def album(reguest):

    albums = Album.objects.all()

    context = {
        'albums': albums
    }
    
    return render(reguest, 'album/index.html', context)