from django.contrib import admin
#from django.contrib.admin.options import ModelAdmin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, Category
# Register your models here.

# category register / admin

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}



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