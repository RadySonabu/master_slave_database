from rest_framework import serializers
from .models import Contact_A00, Contact_A01, Contact_A02, Group_A00, Group_A01


class Contact_A00Serializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Contact_A00
        fields = '__all__'


class Contact_A01Serializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Contact_A01
        fields = '__all__'


class Contact_A02Serializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Contact_A02
        fields = '__all__'


class Group_A00Serializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group_A00
        fields = '__all__'


class Group_A01Serializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group_A01
        fields = '__all__'
