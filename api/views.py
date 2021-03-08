from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Gang
from .serializers import GangSerializers


# Create your views here.

def main(request):
    return HttpResponse('''
    <h1>Woof Gang.</h1>
    <a href='http://127.0.0.1:8000/gang/'>List</a>
    <br>
    <a href='http://127.0.0.1:8000/gang/create'>Create</a>
    
    ''')


class GangList(generics.ListAPIView):
    queryset = Gang.objects.all()
    serializer_class = GangSerializers


class GangCreate(generics.CreateAPIView):
    queryset = Gang.objects.all()
    serializer_class = GangSerializers