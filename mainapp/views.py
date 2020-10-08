from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory


def main(request):
    basket = Basket.objects.filter(user=request.user)
    content = {
        'basket': basket,
    }

    return render(request, 'mainapp/index.html', context=content)


def contacts(request):
    basket = Basket.objects.filter(user=request.user)
    content = {
        'basket': basket,
    }
    return render(request, 'mainapp/contacts.html', context=content)


def catalog(request, pk=None):
    basket = Basket.objects.filter(user=request.user)
    links_menu = ProductCategory.objects.all()

    if pk is not None:
        products = Product.objects.filter(pk=pk)
        content = {
            'products': products,
            'basket': basket,
        }

        return render(request, 'mainapp/lot.html', content)

    products = Product.objects.all()
    title = 'Каталог'
    content = {
        'title': title,
        'links_menu': links_menu,
        'products': products,
        'basket': basket,
    }

    return render(request, 'mainapp/catalog.html', content)


def category(request, pk=None):
    links_menu = ProductCategory.objects.all()
    basket = Basket.objects.filter(user=request.user)
    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
        else:
            products = Product.objects.filter(category__pk=pk)

        content = {
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'basket': basket,
        }

        return render(request, 'mainapp/catalog.html', content)

    same_products = Product.objects.all()

    content = {
        'links_menu': links_menu,
        'products': same_products,
        'basket': basket,
    }

    return render(request, 'mainapp/catalog.html', content)
