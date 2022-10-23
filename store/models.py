from django.contrib.sessions.models import Session
from django.db import models
from django.utils.translation import gettext_lazy as _
from checkout.models import Transaction
from django_store import settings


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    featured = models.BooleanField(default=False)
    order = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = _("Categories")
        verbose_name = _("category")


class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = _("Authors")
        verbose_name = _("Author")


class Product(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.TextField(null=True)
    description = models.TextField(null=True)
    image = models.ImageField()
    pdf_file = models.FileField(null=True)
    price = models.FloatField()
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    
    @property
    def pdf_file_link(self):
        return settings.SITE_URL + self.pdf_file.url

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = _("Products")
        verbose_name = _("Product")


class Orders(models.Model):
    transaction = models.OneToOneField(Transaction, on_delete=models.PROTECT , null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name_plural = _('Orders')
        verbose_name = _('Order')


class OrderProduct(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.id} | create at : {self.created_at}'
    
    
class Cart(models.Model):
    items = models.JSONField(default=dict)
    session = models.ForeignKey(Session, on_delete= models.CASCADE )
    

class Slider(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField(max_length=500)
    image = models.ImageField(null=True)
    order = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = _('Sliders')
        verbose_name = _('Slider')
