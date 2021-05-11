from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
from .models import Post, Comment

class PostAdmin(SummernoteModelAdmin):
    
    list_display = [
        'title',
        'short_desc',
        'description',
        'thumbnail',
        
        
    ]
    summernote_fields = ['description']

admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    
    list_display = [
        'name',
        'body',
        
    ]

admin.site.register(Comment, CommentAdmin)