from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import get_object_or_404, redirect, render
from main import models
from main import forms
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from django.views.decorators.csrf import csrf_protect

# Create your views here.
@login_required(login_url='/login')
def home(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        product_list = models.Product.objects.all()
    else:
        product_list = models.Product.objects.filter(user=request.user)

    data = {
        'name': 'Randuichi Touya',
        'class': 'PBP D',
        'product_list' : product_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'logged_in_user': request.user,
    }

    return render(request, "home.html", data)

@login_required(login_url='/login')
def view_product(request, id):
    product = get_object_or_404(models.Product, pk=id)

    context = {'product': product}

    return render(request,"view_product.html",context)

# Product management

@login_required(login_url='/login') 
def add_product(request):
    form = forms.ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:home')
    
    context = {'form' : form}
    return render(request,"add_product.html",context)

@login_required(login_url='/login') 
def edit_product(request, id):
    prod = get_object_or_404(models.Product, pk=id)
    form = forms.ProductForm(request.POST or None, instance=prod)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:home')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

@login_required(login_url='/login')
def delete_product(request, id):
    prod = get_object_or_404(models.Product, pk=id)
    prod.delete()
    return HttpResponseRedirect(reverse('main:home'))

## User Management
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:home"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

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
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'player' : product.player,
            'club' : product.club,
            'price': product.price,
            'stock': product.stock,
            'user': {
                'username': product.user.username if product.user else None
            }
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)

def show_json_by_id(request, product_id):
    try:
        product = models.Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'price': product.price,
            'stock': product.stock,
            'is_featured': product.is_featured,
            'player' : product.player,
            'club' : product.club,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except models.Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
    

# AJAX Ts
@csrf_exempt
@require_POST
def add_product_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("price")
    stock = request.POST.get("stock")
    description = strip_tags(request.POST.get("description"))
    category = request.POST.get("category")
    thumbnail = strip_tags(request.POST.get("thumbnail"))
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    player = strip_tags(request.POST.get("player"))
    club = strip_tags(request.POST.get("club"))
    user = request.user

    new_product = models.Product(
        name=name, 
        price=price,
        stock=stock,
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        player=player,
        club=club,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
@require_POST
def edit_product_ajax(request, id):
    try:
        product = models.Product.objects.get(pk=id)
    except models.Product.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Product not found'}, status=404)

    # Security Check: Ensure the user owns the product they're trying to edit
    if product.user != request.user:
        return JsonResponse({'status': 'error', 'message': 'Forbidden'}, status=403)

    # Update the product fields from the POST data
    product.name = strip_tags(request.POST.get("name", product.name))
    product.price = request.POST.get("price", product.price)
    product.stock = request.POST.get("stock", product.stock)
    product.description = strip_tags(request.POST.get("description", product.description))
    product.category = request.POST.get("category", product.category)
    product.thumbnail = strip_tags(request.POST.get("thumbnail", product.thumbnail))
    product.is_featured = request.POST.get("is_featured") == 'on'
    product.player = strip_tags(request.POST.get("player", product.player))
    product.club = strip_tags(request.POST.get("club", product.club))
    
    product.save()

    return JsonResponse({'status': 'success', 'message': 'Product updated successfully'})

@csrf_exempt
@require_POST
def delete_product_ajax(request, id):
    try:
        product = models.Product.objects.get(pk=id)
    except models.Product.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Product not found'}, status=404)

    # Security Check: Ensure the user owns the product
    if product.user != request.user:
        return JsonResponse({'status': 'error', 'message': 'Forbidden'}, status=403)

    product.delete()
    return JsonResponse({'status': 'success', 'message': 'Product deleted successfully'})

def register_ajax(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'status': 'success', 
                'message': 'Account created successfully! Please log in.'
            }, status=201)
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

def login_ajax(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response_data = {
                'status': 'success',
                'redirect_url': reverse('main:home')
            }
            response = JsonResponse(response_data)
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


@require_POST
@csrf_protect
def logout_ajax(request):
    logout(request)
    response = JsonResponse({"success": True, "redirect_url": reverse("main:login")})
    response.delete_cookie('last_login')
    return response