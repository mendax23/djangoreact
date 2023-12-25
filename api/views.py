from django.shortcuts import render
from rest_framework import generics
from .models import Room
from .serializers import RoomSerializer

class Roomview(generics.ListAPIView):
    print("i am in RoomView class")
    queryset = Room.objects.all()
    serializer_class = RoomSerializer