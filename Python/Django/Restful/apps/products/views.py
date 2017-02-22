from django.shortcuts import render, redirect
from .models import Product

def index(request):
    context = {
        "products": Product.objects.all()
    }
    return render(request, 'products/index.html', context)

def addnew(request):
    return render(request, 'products/new.html')

def create(request):
    if request.method == 'POST':
        Product.objects.create(name=request.POST['name'], description=request.POST['description'], price=request.POST['price'])
        return redirect('/')

def goback(request):
    return redirect('/')

def show(request, id):
    context = {
        "id": id,
        "product": Product.objects.get(id=id)
    }
    return render(request, 'products/detail.html', context)

def edit(request, id):
    context = {
        "id": id,
        "product": Product.objects.get(id=id)
    }
    return render(request, 'products/edit.html', context)

def remove(request, id):
    Product.objects.get(id=id).delete()
    return redirect('/')

def update(request, id):
    Product.objects.filter(id=id).update(name=request.POST['name'], description=request.POST['description'], price=request.POST['price'])
    return redirect('/')
