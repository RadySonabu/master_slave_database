from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import viewsets, status, filters
from django.db.models.signals import post_save, pre_save
from .models import Contact_A00, Contact_A01, Contact_A02, Group_A00, Group_A01
from contact_slave.models import Contact_A00Slave, Contact_A01Slave, Contact_A02Slave, Group_A00Slave, Group_A01Slave
from .serializers import Contact_A00Serializer, Contact_A01Serializer, Contact_A02Serializer, Group_A00Serializer, Group_A01Serializer


class Contact_A00View(viewsets.ModelViewSet):
    queryset = Contact_A00.objects.all()
    serializer_class = Contact_A00Serializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        Contact_A00Slave.objects.create(contact_a00_rec=instance, contact_id=data['contact_id'], first_name=data['first_name'], middle_initial=data['middle_initial'],
                                        last_name=data['last_name'], address_1=data['address_1'], barangay_district=data['barangay_district'],
                                        city_municipality=data['city_municipality'],
                                        postal_code=data['postal_code'],
                                        province=data['province'],
                                        phone_1=data['phone_1'],
                                        phone_2=data['phone_2'],
                                        email=data['email'],
                                        status=False,
                                        )

        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        contact = self.get_object()
        contact.status = False
        contact.save()
        return Response(data='delete success')


class Contact_A01View(viewsets.ModelViewSet):
    queryset = Contact_A01.objects.all()
    serializer_class = Contact_A01Serializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        Contact_A01Slave.objects.create(
            contact_a01_rec=instance, contact_id=data['contact_id'], skill_id=data['skill_id'], comments=data['comments'], status=False,)

        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        contact = self.get_object()
        contact.status = False
        contact.save()
        return Response(data='delete success')


class Contact_A02View(viewsets.ModelViewSet):
    queryset = Contact_A02.objects.all()
    serializer_class = Contact_A02Serializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        Contact_A02Slave.objects.create(
            contact_a02_rec=instance, contact_id=data['contact_id'], endorsement_id=data['endorsement_id'], message=data['message'], status=False,)

        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        contact = self.get_object()
        contact.status = False
        contact.save()
        return Response(data='delete success')


class Group_A00View(viewsets.ModelViewSet):
    queryset = Group_A00.objects.all()
    serializer_class = Group_A00Serializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        Group_A00Slave.objects.create(group_a00_rec=instance, group_id=data['group_id'], first_name=data['first_name'], middle_initial=data['middle_initial'],
                                      last_name=data['last_name'], address_1=data['address_1'], barangay_district=data['barangay_district'],
                                      city_municipality=data['city_municipality'],
                                      postal_code=data['postal_code'],
                                      province=data['province'],
                                      phone_1=data['phone_1'],
                                      phone_2=data['phone_2'],
                                      email=data['email'],
                                      status=False,
                                      )

        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        contact = self.get_object()
        contact.status = False
        contact.save()
        return Response(data='delete success')


class Group_A01View(viewsets.ModelViewSet):
    queryset = Group_A01.objects.all()
    serializer_class = Group_A01Serializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        Group_A01Slave.objects.create(
            group_a01_rec=instance, group_id=data['group_id'], contact_id=data['contact_id'], group_role=data['group_role'], comments=data['comments'], status=False,)

        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        contact = self.get_object()
        contact.status = False
        contact.save()
        return Response(data='delete success')
