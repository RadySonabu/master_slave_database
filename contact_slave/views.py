from django.shortcuts import render
from rest_framework import viewsets
from .models import Contact_A00Slave, Contact_A01Slave, Contact_A02Slave, Group_A00Slave, Group_A01Slave
from .serializers import Contact_A00SlaveSerializer, Contact_A01SlaveSerializer, Contact_A02SlaveSerializer, Group_A00SlaveSerializer, Group_A01SlaveSerializer


class Contact_A00View(viewsets.ModelViewSet):
    queryset = Contact_A00Slave.objects.all()
    serializer_class = Contact_A00SlaveSerializer


class Contact_A01View(viewsets.ModelViewSet):
    queryset = Contact_A01Slave.objects.all()
    serializer_class = Contact_A01SlaveSerializer


class Contact_A02View(viewsets.ModelViewSet):
    queryset = Contact_A02Slave.objects.all()
    serializer_class = Contact_A02SlaveSerializer


class Group_A00View(viewsets.ModelViewSet):
    queryset = Group_A00Slave.objects.all()
    serializer_class = Group_A00SlaveSerializer


class Group_A01View(viewsets.ModelViewSet):
    queryset = Group_A01Slave.objects.all()
    serializer_class = Group_A01SlaveSerializer
