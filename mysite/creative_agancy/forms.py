from django import forms
from .models import *


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category()
        fields = '__all__'


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service()
        fields = '__all__'


class PricingForm(forms.ModelForm):
    class Meta:
        model = Pricing()
        fields = '__all__'


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team()
        fields = '__all__'


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial()
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product()
        fields = '__all__'


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact()
        fields = '__all__'
