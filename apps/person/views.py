from rest_framework import authentication, permissions, viewsets

from .models import Person
from .serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Person to be viewed or edited.
    """

    http_method_names = ["get", "post", "patch", "delete"]
    authentication_classes = [
        authentication.TokenAuthentication,
        authentication.SessionAuthentication,
    ]
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get_permissions(self):
        """ Only admin user CRUD operations """
        permission_classes = []
        if self.action not in ["list", "retrieve"]:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
