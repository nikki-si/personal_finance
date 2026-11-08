from django.urls import path

from . import views

app_name = "transactions"

urlpatterns = [
    path("", views.transaction_list, name="list"),
    path("<int:pk>/", views.transaction_detail, name="detail"),
    path("by-category/", views.transaction_by_category, name="by_category"),
    path("over/", views.transaction_over, name="over"),
    path("top/", views.transaction_top, name="top"),
]
