from django.contrib import admin
from .models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    #readonly_fields = ('created', 'updated')
    pass

admin.site.register(Contact, ContactAdmin)