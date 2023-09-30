from django.contrib import admin
from django.urls import path, include
from .views import products_details_view, products_list_create_view, product_update_view, product_destroy_view, product_mixin_view

urlpatterns = [ #method 1
    path('', products_list_create_view),
    path('<int:pk>/', products_details_view),
    path('<int:pk>/update/', product_update_view),
    path('<int:pk>/delete/', product_destroy_view),
]

# urlpatterns = [     # method 2
#     path('', product_mixin_view),
#     path('<int:pk>/', product_mixin_view)
# ]