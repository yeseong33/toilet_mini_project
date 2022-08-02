from rest_framework import serializers
from .models import Toilet

class ToiletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toilet
        exclude = ("modified",)
        read_only_fields = ("id", "created", "updated")

    def create(self, data):
        request = self.context.get("request")
        toilet = Toilet.objects.create(**data)
        return toilet