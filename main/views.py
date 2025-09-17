from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import get_object_or_404, redirect, render
from main import models
from main import forms

# Create your views here.
def home(request):
    product_list = models.Product.objects.all()

    data = {
        'name': 'Randuichi Touya',
        'class': 'PBP D',
        'product_list' : product_list,
    }

    return render(request, "home.html", data)

def add_product(request):
    form = forms.ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:home')
    
    context = {'form' : form}
    return render(request,"add_product.html",context)

def view_product(request, id):
    product = get_object_or_404(models.Product, pk=id)

    context = {'product': product}

    return render(request,"view_product.html",context)

## View via HttpResponse

def show_xml(request):
    product_list = models.Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_xml_by_id(request, product_id):
   try:
       product_item = models.Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except models.Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json(request):
    product_list = models.Product.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")

def show_json_by_id(request, product_id):
   try:
       news_item = models.Product.objects.get(pk=product_id)
       json_data = serializers.serialize("json", [news_item])
       return HttpResponse(json_data, content_type="application/json")
   except models.Product.DoesNotExist:
       return HttpResponse(status=404)