from django.shortcuts import render, redirect
from .services import *
from .forms import *
from .models import *


def home(request):
    model = Contact()
    form = ContactForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
    service = get_services()
    teams = get_teams()
    categories = get_categories()
    pricing = get_pricing()
    testimonial = get_testimonials()
    clients = get_clients()
    products=get_products()
    ctx = {
        'service': service,
        'teams': teams,
        'categories': categories,
        'pricing': pricing,
        'testimonial': testimonial,
        'clients': clients,
        'products':products

    }
    return render(request, 'index.html', ctx)

def product(request,category_id):
    products=get_category_by_id(category_id=category_id)
    ctx={
        'products':products
    }
    return render(request,'product.html',ctx)