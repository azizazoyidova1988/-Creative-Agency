from django.urls import path, include
from creative_agancy import views

urlpatterns = [
    path('', views.home, name='home')
]
