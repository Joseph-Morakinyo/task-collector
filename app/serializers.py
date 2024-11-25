from rest_framework.serializers import ModelSerializer, Serializer
from .models import User, OneTimePassword


class RegisterUserSerializers(ModelSerializer):
    class meta:
        model = User
        fields = (
            "first_name", 
            "last_name",
            "email",
            "password"
            "device_id"
            )

    
