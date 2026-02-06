from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="Stocks Home"),
    path("strategies", views.strategies, name="Strategies"),
    path("<slug:stock_id>", views.stock, name="Stock"),
]