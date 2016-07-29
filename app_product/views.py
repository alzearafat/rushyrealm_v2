import datetime
from django.utils import timezone
from app_product.models import Product
from django.core.urlresolvers import reverse
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def product_list_all(request):
    product_list_all    = Product.objects.all().order_by('-tanggal_publish')
    paginator           = Paginator(product_list_all, 12)
    page                = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'app_product/product_homepage.html', {"products": products})

# def product_list_kaos(request):
#     product_list        = Product.objects.filter(kategori_id=5).order_by('-tanggal_publish')
#     paginator           = Paginator(product_list, 12)
#     page                = request.GET.get('page')
#     try:
#         products = paginator.page(page)
#     except PageNotAnInteger:
#         products = paginator.page(1)
#     except EmptyPage:
#         products = paginator.page(paginator.num_pages)
#     return render(request, 'app_product/product_list_kaos.html', {"products": products})

def product_single(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'app_product/product_single.html', {'product': product})

def product_about(request):
    return render(request, 'app_product/product_about.html')

def product_contact(request):
    return render(request, 'app_product/product_contact.html')