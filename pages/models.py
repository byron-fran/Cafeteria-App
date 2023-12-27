from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Pages(models.Model):

    title = models.CharField(verbose_name='title', max_length=200)
    content = RichTextField(verbose_name='Description',null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now= True)
    order = models.SmallIntegerField(default=0, verbose_name='order')
    class Meta:
        verbose_name='title'
        verbose_name_plural='titles'
        ordering = ['order', 'title']
    def __str__(self):
        return  self.title