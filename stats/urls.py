from django.urls import path
from transactions import views as transaction_views

app_name = "stats"

urlpatterns = [
    path("", transaction_views.statistics_view, name="statistics"),
    path("expensive/", transaction_views.expensive_categories, name="expensive"),
]
