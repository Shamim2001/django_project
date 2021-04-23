from django.shortcuts import render

from .models import Profile

# Create your views here.
 
def homepage(reguest):

    profile = Profile.objects.all()

    context = {
        'profile': profile
    }
    
    return render(reguest, 'index.html', context)