from django.shortcuts import render


def main(request):
    return render(request, 'mainapp/index.html')


def catalog(request):
    return render(request, 'mainapp/catalog.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')


def lot_1(request):
    return render(request, 'mainapp/catalog/lot_1.html')


def lot_2(request):
    return render(request, 'mainapp/catalog/lot_2.html')


def lot_3(request):
    return render(request, 'mainapp/catalog/lot_3.html')
