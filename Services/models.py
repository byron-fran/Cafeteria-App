from django.db import models

# Create your models here.

class Service(models.Model):
    
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    content = models.TextField(null=True, blank=True)
    image = models.FileField( upload_to='services',verbose_name='image')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now= True)
    
    class Meta:
        verbose_name = 'service'
        verbose_name_plural = 'services'
        ordering = ['-created']
        
    def __str__(self):
        return self.title    