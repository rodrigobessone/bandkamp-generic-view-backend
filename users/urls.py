from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)


urlpatterns = [
    path("users/", views.UserView.as_view()),
    path("users/<int:pk>/", views.UserDetailView.as_view()),
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
    path("docs/", SpectacularAPIView.as_view(), name="docs"),
    path("docs/swagger-ui/", SpectacularSwaggerView.as_view(url_name="docs"), name="swagger-ui"),
    path("docs/redoc/", SpectacularRedocView.as_view(url_name="docs"), name="redoc"),
]
