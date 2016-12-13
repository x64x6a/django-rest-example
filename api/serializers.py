from rest_framework.serializers import ModelSerializer

from api.models import Car


class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'make', 'model', 'color', 'year', 'owner')