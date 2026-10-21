from django.urls import path

from . import views

urlpatterns = [
    path("", views.transactions_list, name="transactions_list"),
    path("<int:transaction_id>/", views.transaction_detail, name="transaction_detail"),
]