from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_page, name="dashboard"),
    path('login/', views.dashboard_login, name="login"),
    path('logout/', views.dashboard_logout, name="logout"),

    path('service/list/', views.services_list, name="services_list"),
    path('service/add/', views.services_create, name="services_add"),
    path('service/<int:service_id>/edit/', views.services_edit, name="services_edit"),
    path('service/<int:service_id>/delete/', views.services_delete, name="services_delete"),

    path('category/list/', views.categories_list, name="categories_list"),
    path('category/add/', views.categories_create, name="categories_add"),
    path('category/<int:category_id>/edit/', views.categories_edit, name="categories_edit"),
    path('category/<int:category_id>/delete/', views.categories_delete,name="categories_delete"),

    path('product/list/', views.products_list, name="products_list"),
    path('product/add/', views.products_create, name="products_add"),
    path('product/<int:product_id>/edit/', views.products_edit, name="products_edit"),
    path('product/<int:product_id>/delete/', views.products_delete, name="products_delete"),

    path('team/list/', views.teams_list, name="teams_list"),
    path('team/add/', views.teams_create, name="teams_add"),
    path('team/<int:team_id>/edit/', views.teams_edit, name="teams_edit"),
    path('team/<int:team_id>/delete/', views.teams_delete, name="teams_delete"),

    path('pricing/list/', views.pricing_list, name="pricing_list"),
    path('pricing/add/', views.pricing_create, name="pricing_add"),
    path('pricing/<int:price_id>/edit/', views.pricing_edit, name="pricing_edit"),
    path('pricing/<int:price_id>/delete/', views.pricing_delete, name="pricing_delete"),

    path('testimonial/list/', views.testimonials_list, name="testimonials_list"),
    path('testimonial/add/', views.testimonials_create, name="testimonials_add"),
    path('testimonial/<int:testimonial_id>/edit/', views.testimonials_edit, name="testimonials_edit"),
    path('testimonial/<int:testimonial_id>/delete/', views.testimonials_delete, name="testimonials_delete"),

   ]