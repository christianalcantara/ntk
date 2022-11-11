from rest_framework import authentication, permissions, serializers, viewsets

from .models import Car
from .serializers import CarSerializer
from ..person.models import Person


class CarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Car to be viewed or edited.
    """

    http_method_names = ["get", "post", "patch", "delete"]
    authentication_classes = [
        authentication.TokenAuthentication,
        authentication.SessionAuthentication,
    ]
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_permissions(self):
        """ Only admin user CRUD operations """
        permission_classes = []
        if self.action not in ["list", "retrieve"]:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    @staticmethod
    def _check_sale_opportunity(person_pk):
        if person_pk:
            try:
                person = Person.objects.get(id=person_pk)
                is_sale_opportunity = person.sale_opportunity
                if not is_sale_opportunity:
                    raise serializers.ValidationError(
                        {"person": "Is not sale opportunity."}
                    )
            except Person.DoesNotExist:
                ...

    def update(self, request, *args, **kwargs):
        person_pk = request.data.get("person")
        self._check_sale_opportunity(person_pk)

        response = super().update(request, *args, **kwargs)
        return response

    def create(self, request, *args, **kwargs):
        person_pk = request.data.get("person")
        self._check_sale_opportunity(person_pk)
        response = super().create(request, *args, **kwargs)
        return response
