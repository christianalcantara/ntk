from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from rest_framework.authtoken import views
from rest_framework_swagger.views import get_swagger_view

from config.api import api

schema_view = get_swagger_view(title="Nork-Town Cars")

urlpatterns = [
    path("", schema_view),
    path("admin/", admin.site.urls, name="admin"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("api/", include(api.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api-token-auth/", views.obtain_auth_token),
]
