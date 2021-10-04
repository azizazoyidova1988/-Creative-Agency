from django.urls import path, include
from creative_agancy import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:category_id>/product', views.product, name='product'),
    path('dashboard/',include('dashboard.urls')),
]
