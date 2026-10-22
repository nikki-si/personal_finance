from django.urls import path

from . import views

app_name = "transactions"

urlpatterns = [
    path("", views.transactions_list, name="list"),
    path("by-category/", views.transactions_by_category, name="by_category"),
    path("over/", views.transactions_over, name="over"),
    path("<int:transaction_id>/", views.transaction_detail, name="detail"),
    path("top/", views.transactions_top, name="top"),
]
