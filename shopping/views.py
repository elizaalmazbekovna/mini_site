from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse,FileResponse
from .models import Product
from django.conf import settings
# Create your views here.

def say_hello(request):
    return HttpResponse('<h1>HELLO WORLD I AM ELIZA</h1>')

def saw_date(request):
    today = datetime.now()
    return HttpResponse(f"Today : {str(today)}")


def main_page(request):
    products = Product.objects.all()
    print(products)
    for i in products:
        print('ID: ',i.id)
        print('title: ',i.title)
        print('price: ',i.price)
    data = {
        'title': 'Главная страница',
        'list': [1,2,3,4,5],
        'product_list': products
    }
    return render(request,'index.html',context=data)


def product_item_view(request,product_id):
    product = Product.objects.get(id=product_id)
    data ={
        'product':product,
        'title':product.title
    }
    return render(request,'item.html', context=data)

def image_view(request):
    path = settings.BASE_DIR/ 'static'/ '123.jpg'
    file = open(path,'rb')
    return FileResponse(file)

