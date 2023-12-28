from django.shortcuts import render
from .models import Product
# Create your views here.
def product(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_detail.html', {'product': product})