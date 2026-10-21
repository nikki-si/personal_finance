from django.urls import path

from . import views

app_name = "transactions"

urlpatterns = [
    path("", views.transactions_list, name="list"),
    path("<int:transaction_id>/", views.transaction_detail, name="detail"),
]
