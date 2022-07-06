from django.urls import path
from . import views

urlpatterns = [
    path('',views.ProductsView.as_view()),
    path('scrap/',views.ScrapView.as_view())
]
