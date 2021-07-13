from django.contrib import admin

from .models import Carousel, Freature
# Register your models here.

class CarouselAdmin(admin.ModelAdmin):

    list_display = [
        'title',
        'short_desc',
        'thumbnail',
        'description'
    ]

admin.site.register(Carousel, CarouselAdmin)


class FreatureAdmin(admin.ModelAdmin):

    list_display = [
        'post',
        'image',
        'description'
    ]

admin.site.register(Freature, FreatureAdmin)

