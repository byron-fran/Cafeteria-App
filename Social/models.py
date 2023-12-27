from django.db import models

# Create your models here.
class Social(models.Model):
    key = models.SlugField(verbose_name='key name', max_length=100, unique=True)
    name = models.CharField(verbose_name='social media', max_length=200)
    url = models.URLField(verbose_name='Url', max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now= True)
    
    class Meta:
        verbose_name='link'
        verbose_name_plural='links'
        ordering = ['-created']
    def __str__(self):
        return  self.name    