from django.shortcuts import render
from product.models import Category, Product


def index(request):
    products = Product.objects.filter(is_sold=False)[:6]
    categories = Category.objects.all()
    active_item = request.path
    context = {
        'categories': categories,
        'products': products,
        'active_item': active_item
    }
    return render(request, 'core/index.html', context)


def about(request):
    active_item = request.path
    context = {'active_item': active_item}
    return render(request, 'core/about.html', context)


def contact(request):
    active_item = request.path
    context = {'active_item': active_item}
    return render(request, 'core/contact.html', context)
