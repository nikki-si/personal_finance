from django.contrib import admin
from .models import Category, Transaction


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("id", "amount", "category", "description", "created_at")
    list_filter = ("category", "created_at")
    search_fields = ("description", "category__name")
    list_select_related = ("category",)
