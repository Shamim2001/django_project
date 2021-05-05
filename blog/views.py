from django.shortcuts import render

from .models import Post

# Create your views here.
 
def blog_list(reguest):

    posts = Post.objects.all()

    context = {
        'posts': posts
    }
    
    return render(reguest, 'blog/index.html', context)