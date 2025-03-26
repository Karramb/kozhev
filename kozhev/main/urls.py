from django.urls import path

from . import views
from main.views import application_view

app_name = 'main'

urlpatterns = [
    path(
        '',
        views.IndexListViews.as_view(),
        name='index'
    ),
    path(
        'products/<int:post_pk>/',
        views.ProductDetailView.as_view(),
        name='product_detail'
    ),
    path('about/', views.About.as_view(), name='about'),
    path('delivery/', views.Delivery.as_view(), name='delivery'),
    path('application/', application_view, name='application'),
]
