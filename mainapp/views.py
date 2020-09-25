from django.shortcuts import render
import json

with open('static/json/context.json', 'r', encoding='UTF-8') as file:
    data = json.load(file)


def main(request):
    return render(request, 'mainapp/index.html', context=data['content'][0]['main'][0])


def catalog(request):
    return render(request, 'mainapp/catalog.html', context=data['content'][0]['catalog'][0])


def contacts(request):
    return render(request, 'mainapp/contacts.html', context=data['content'][0]['contacts'][0])


def lot_1(request):
    return render(request, 'mainapp/catalog/lot_1.html', context=data['content'][0]['lot_1'][0])


def lot_2(request):
    return render(request, 'mainapp/catalog/lot_2.html', context=data['content'][0]['lot_2'][0])


def lot_3(request):
    return render(request, 'mainapp/catalog/lot_3.html', context=data['content'][0]['lot_3'][0])
