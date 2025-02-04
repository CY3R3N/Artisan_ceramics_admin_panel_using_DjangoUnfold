from django.urls import path
from .views import CatalogListView, CatalogDetailView

urlpatterns = [
    path('catalog/', CatalogListView.as_view(), name='catalog-list'),
    path('catalog/<int:pk>/', CatalogDetailView.as_view(), name='catalog-detail'),
]