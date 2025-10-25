from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='list'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='detail'),
    path('product/add/', views.ProductCreateView.as_view(), name='add'),
    path('product/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='edit'),
    path('product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='delete'),
]
