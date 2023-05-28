from django.shortcuts import render, get_object_or_404
from .models import Product


def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.filter(
        category=product.category,
        is_sold=False,
    ).exclude(pk=pk)[:3]
    context = {
        'product': product,
        'related_products': related_products
    }

    return render(request, 'product/product_detail.html', context)
