from rest_framework.serializers import ModelSerializer

from hackathon.models import Cargo

class CargoSerializer(ModelSerializer):
    class Meta:
        model = Cargo
        fields = "__all__"