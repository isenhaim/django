from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory


def main(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        price = 0
        count = 0
        for i in basket:
            price += i.get_cost()
            count += i.get_count()

        content = {
            'basket': basket,
            'price': price,
            'count': count,
        }
    else:
        content = {
            'basket': basket,
        }

    return render(request, 'mainapp/index.html', context=content)


def contacts(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        price = 0
        count = 0
        for i in basket:
            price += i.get_cost()
            count += i.get_count()
    content = {
        'basket': basket,
        'price': price,
        'count': count,
    }
    return render(request, 'mainapp/contacts.html', context=content)


def catalog(request, pk=None):
    links_menu = ProductCategory.objects.all()
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        price = 0
        count = 0
        for i in basket:
            price += i.get_cost()
            count += i.get_count()
    if pk is not None:
        products = Product.objects.filter(pk=pk)
        content = {
            'products': products,
            'basket': basket,
            'price': price,
            'count': count,
        }

        return render(request, 'mainapp/lot.html', content)

    products = Product.objects.all()
    title = 'Каталог'
    content = {
        'title': title,
        'links_menu': links_menu,
        'products': products,
        'basket': basket,
        'price': price,
        'count': count,
    }

    return render(request, 'mainapp/catalog.html', content)


def category(request, pk=None):
    links_menu = ProductCategory.objects.all()

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        price = 0
        count = 0
        for i in basket:
            price += i.get_cost()
            count += i.get_count()

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
            'price': price,
            'count': count,
        }

        return render(request, 'mainapp/catalog.html', content)

    same_products = Product.objects.all()

    content = {
        'links_menu': links_menu,
        'products': same_products,
        'basket': basket,
        'price': price,
        'count': count,

    }

    return render(request, 'mainapp/catalog.html', content)
