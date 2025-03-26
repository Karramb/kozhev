from django.contrib import admin
from django.contrib.auth.models import Group

from main.models import Category, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price'
    )
    search_fields = (
        'name',
        'price'
    )
    list_filter = (
        'name',
        'price'
    )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'slug'
    )
    search_fields = (
        'title',
        'slug'
    )
    list_filter = (
        'title',
        'slug'
    )

admin.site.unregister(Group)
