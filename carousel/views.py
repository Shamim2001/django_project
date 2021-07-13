from django.shortcuts import render

from .models import Carousel, Freature
# Create your views here.
 
def carousel(reguest):

    carousel = Carousel.objects.all()
    freature = Freature.objects.all()[:3]

    context = {
        'carousel': carousel,
        'freature': freature
    }
    
    return render(reguest, 'carousel/index.html', context)

