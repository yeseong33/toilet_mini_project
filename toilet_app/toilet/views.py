from http.client import HTTPResponse
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from toilet.models import Toilet
from toilet.serializers import ToiletSerializer

class ToiletsView(ModelViewSet):

    queryset = Toilet.objects.all()
    serializer_class = ToiletSerializer