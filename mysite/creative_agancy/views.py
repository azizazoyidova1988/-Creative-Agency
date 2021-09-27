from django.shortcuts import render, redirect
from .services import *
from .forms import *
from .models import *


def home(request):
    service = get_services()
    teams=get_teams()
    categories=get_categories()
    ctx = {
        'service': service,
        'teams':teams,
        'categories':categories
    }
    return render(request, 'index.html', ctx)
