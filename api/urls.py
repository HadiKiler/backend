from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token
# from rest_framework_simplejwt.views import (
# #     TokenObtainPairView,
# #     TokenRefreshView,
# #     TokenVerifyView,
# # )

from . import views
# from .views import api_home


urlpatterns = [
    path('', views.api_home),    # localhost:8000/api/
    path('auth/', obtain_auth_token),
    path('products/', include('products.urls'))
]
