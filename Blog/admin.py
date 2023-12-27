from django.contrib import admin
from . import models
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class PostAdmin(admin.ModelAdmin):
    readonly_fields =  ('created', 'updated')
    list_display = ('title', 'author', 'post_categories')
    ordering = ('author', 'published')
    search_fields = ('title', 'author__username')
    list_filter=('author__username', 'categories__name')
    
    #add list display
    def post_categories(self, obj):
        return ','.join([ c.name for c  in obj.categories.all().order_by('name')])
    
    post_categories.short_description = 'Categories'
    
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Post, PostAdmin)