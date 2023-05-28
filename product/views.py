from django.shortcuts import render, get_list_or_404
from .models import Product


def detail(request, pk):
    product = get_list_or_404(Product, pk=pk)
    context = {'product': product}
    print(context)

    return render(request, 'product/product_detail.html', context)
