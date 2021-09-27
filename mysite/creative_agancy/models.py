from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    description = models.CharField(max_length=450, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "service"
    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    job = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=450, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "team"
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    project_name = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=450, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "category"
    def __str__(self):
        return self.name


class Pricing(models.Model):
    price_type = models.CharField(max_length=40, blank=False, null=False)
    price = models.CharField(max_length=20, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "pricing"
    def __str__(self):
        return self.price_type


class Testimonial(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    job = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=450, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "testimonial"
    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    phone = models.CharField(max_length=50, blank=False, null=False)
    message = models.CharField(max_length=450, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "contact"
    def __str__(self):
        return self.name
