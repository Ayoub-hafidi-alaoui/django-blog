from django.db import models

# Create your models here.

'''
    title
    content 
    image
    tags
'''

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='posts/assets/images')
    
    def __str__(self):
        return self.title
    
    
