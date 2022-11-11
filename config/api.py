from rest_framework import routers

from apps.car.views import CarViewSet
from apps.person.views import PersonViewSet
from apps.users.views import UserViewSet

# Settings
api = routers.DefaultRouter()
api.trailing_slash = "/?"

# Users API
api.register(r"users", viewset=UserViewSet, basename="users")

# Person API
api.register(r"person", PersonViewSet)

# Car API
api.register(r"car", CarViewSet)
