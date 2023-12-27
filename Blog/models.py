from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now= True)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['-created']
        
    def __str__(self):
       return self.name

   
class Post(models.Model):
    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.TextField(verbose_name='content')
    published = models.DateField(verbose_name= 'date creation', default=now)
    image = models.FileField( upload_to='blogs',verbose_name='image')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now= True)
    categories = models.ManyToManyField(Category, verbose_name='categories')
    
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'post'
        ordering = ['-created']
        
    def __str__(self):
       return self.title