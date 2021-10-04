from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from creative_agancy.models import Service, Team, Testimonial, Contact, Category, Product, \
    Pricing
from creative_agancy.forms import *
from . import services


def login_required_decorator(f):
    return login_required(f, login_url="login")


@login_required_decorator
def dashboard_page(request):
    category = services.get_categories_count()
    print(category)
    products_count = services.get_products_count()
    teams_count = services.get_teams_count()
    services_count = services.get_services_count()
    category_product=services.get_categories_products_count()


    ctx = {
        "category": category,
        "products_count":  products_count,
        "teams_count": teams_count,
        "services_count": services_count,
        "category_product": category_product,

    }
    return render(request, 'dashboard/index.html',ctx)


def dashboard_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'dashboard/login.html')


@login_required_decorator
def dashboard_logout(request):
    logout(request)
    return redirect('login')


@login_required_decorator
def categories_list(request):
    categories = services.get_categories()
    ctx = {
        "categories": categories
    }
    return render(request, 'dashboard/category/list.html', ctx)


@login_required_decorator
def categories_create(request):
    model = Category()
    form = CategoryForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('categories_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/category/form.html', ctx)


@login_required_decorator
def categories_edit(request, category_id):
    model = Category.objects.get(id=category_id)
    form = CategoryForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('categories_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/category/form.html', ctx)

@login_required_decorator
def categories_delete(request, category_id):
    model = Category.objects.get(id=category_id)
    model.delete()
    return redirect("categories_list")

@login_required_decorator
def services_list(request):
    service = services.get_service()
    ctx = {
        "services": service
    }
    return render(request, 'dashboard/service/list.html', ctx)

@login_required_decorator
def services_create(request):
    model = Service()
    form = ServiceForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('services_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/service/form.html', ctx)

@login_required_decorator
def services_edit(request, service_id):
    model = Service.objects.get(id=service_id)
    form = ServiceForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('services_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/service/form.html', ctx)

@login_required_decorator
def services_delete(request, service_id):
    model = Service.objects.get(id=service_id)
    model.delete()
    return redirect("services_list")

@login_required_decorator
def teams_list(request):
    teams = services.get_teams()
    ctx = {
        "teams": teams
    }
    return render(request, 'dashboard/team/list.html', ctx)

@login_required_decorator
def teams_create(request):
    model = Team()
    form = TeamForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('teams_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/team/form.html', ctx)

@login_required_decorator
def teams_edit(request, team_id):
    model = Team.objects.get(id=team_id)
    form = TeamForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('teams_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/team/form.html', ctx)

@login_required_decorator
def teams_delete(request, team_id):
    model = Team.objects.get(id=team_id)
    model.delete()
    return redirect("teams_list")

@login_required_decorator
def products_list(request):
    products = services.get_products()
    ctx = {
        "products": products
    }
    return render(request, 'dashboard/product/list.html', ctx)

@login_required_decorator
def products_create(request):
    model = Product()
    form = ProductForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('products_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/product/form.html', ctx)

@login_required_decorator
def products_edit(request, product_id):
    model = Product.objects.get(id=product_id)
    form = ProductForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('products_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/product/form.html', ctx)

@login_required_decorator
def products_delete(request, product_id):
    model = Product.objects.get(id=product_id)
    model.delete()
    return redirect("products_list")

@login_required_decorator
def pricing_list(request):
    pricing = services.get_pricing()
    ctx = {
        "pricing": pricing
    }
    return render(request, 'dashboard/pricing/list.html', ctx)

@login_required_decorator
def pricing_create(request):
    model = Pricing()
    form = PricingForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('pricing_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/pricing/form.html', ctx)

@login_required_decorator
def pricing_edit(request, price_id):
    model = Pricing.objects.get(id=price_id)
    form = PricingForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('pricing_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/pricing/form.html', ctx)

@login_required_decorator
def pricing_delete(request, price_id):
    model = Pricing.objects.get(id=price_id)
    model.delete()
    return redirect("pricing_list")

@login_required_decorator
def testimonials_list(request):
    testimonials = services.get_testimonial()
    ctx = {
        "testimonials": testimonials
    }
    return render(request, 'dashboard/testimonial/list.html', ctx)

@login_required_decorator
def testimonials_create(request):
    model = Testimonial()
    form = TestimonialForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('testimonials_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/testimonial/form.html', ctx)

@login_required_decorator
def testimonials_edit(request, testimonial_id):
    model = Testimonial.objects.get(id=testimonial_id)
    form = TeamForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('testimonials_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/testimonial/form.html', ctx)

@login_required_decorator
def testimonials_delete(request, testimonial_id):
    model = Testimonial.objects.get(id=testimonial_id)
    model.delete()
    return redirect("testimonials_list")
