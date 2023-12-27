from django.shortcuts import render, get_list_or_404
from .models import Post
from .models import Category

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request, ('blog.html'), {'posts': posts})


def category(request, category_id):
    #category = get_list_or_404(Category, id=category_id)
    category = Category.objects.filter(id=category_id)

    return render(request, 'category.html',{'category': category})