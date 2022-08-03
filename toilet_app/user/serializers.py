from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("modified",)
        read_only_fields = ("id", "created", "updated")
    
    def create(self, data):
        request = self.context.get("request")
        user = User.objects.create(**data)
        return user
