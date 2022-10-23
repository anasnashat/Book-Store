from django.contrib import admin

from checkout import models


# Register your models here.

@admin.register(models.Transaction)
class Transaction(admin.ModelAdmin):
    list_per_page = 20
    