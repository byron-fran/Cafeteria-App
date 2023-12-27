from django.contrib import admin
from .models import Social

# Register your models here.
class SocialAdmin(admin.ModelAdmin):
   readonly_fields = ('created', 'updated')
   
   def get_readonly_fields(self, request, obj=None):
       if request.user.groups.filter(name='Personal').exists():
           return ('key', 'url', 'created', 'updated')
       else:
           return ('created', 'updated')
   
admin.site.register(Social, SocialAdmin)   