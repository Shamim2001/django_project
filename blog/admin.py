from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    
    list_display = [
        'title',
        'short_desc',
        'description',
        'thumbnail',
        
        
    ]

admin.site.register(Post, PostAdmin)