from django.db import models

# Create your models here.
class Post(models.Model):
    
    title = models.CharField(max_length=100)
    short_desc = models.TextField()
    thumbnail = models.ImageField(upload_to='imge/photo')
    
    description = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)