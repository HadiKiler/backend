from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token
# from rest_framework_simplejwt.views import (
# #     TokenObtainPairView,
# #     TokenRefreshView,
# #     TokenVerifyView,
# # )

from . import views
# from .views import api_home
from products.viewsets import ProductViewSet

urlpatterns = [
    path('', views.api_home),    # localhost:8000/api/
    path('auth/', obtain_auth_token),
    path('search/', include('search.urls')),
    path('products/', include('products.urls')),
    path('v2/', include('api.routers'))
]
