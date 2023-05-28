from django.shortcuts import render
from product.models import Category, Product


def index(request):
    products = Product.objects.filter(is_sold=False)[:6]
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'core/index.html', context)


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')
