from django.shortcuts import render
from .models import Pages
# Create your views here.
def pages(request, page_id,name_slug):
    page = Pages.objects.get(id=page_id)
    return render(request, 'sample.html', {'page': page})