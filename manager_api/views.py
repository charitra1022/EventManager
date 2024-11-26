from django.shortcuts import render
from rest_framework import viewsets

from .serializers import SampleModelSerializer
from .models import SampleModel

class SampleViewSet(viewsets.ModelViewSet):
    queryset = SampleModel.objects.all()
    serializer_class = SampleModelSerializer
    