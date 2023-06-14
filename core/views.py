from django.shortcuts import render
from rest_framework import generics
from .serializers import LedSerializer
from .models import Led

class LededitApiView(generics.RetrieveUpdateAPIView):
    serializer_class = LedSerializer
    queryset = Led.objects.all()


class LedCreateApiView(generics.CreateAPIView):
    serializer_class = LedSerializer
    queryset = Led.objects.all()
    