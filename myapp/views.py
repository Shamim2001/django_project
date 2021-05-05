from django.shortcuts import render

from .models import Profile

# Create your views here.
 
def homepage(reguest):

    profile = Profile.objects.all()

    context = {
        'profile': profile
    }
    
    return render(reguest, 'index.html', context)

#blueberry.html index link

def blueberry(reguest):
    
    

    context = {
        
    }
    
    return render(reguest, 'blueberry.html', context)