from rest_framework import serializers
from .models import Contact_A00Slave, Contact_A01Slave, Contact_A02Slave, Group_A00Slave, Group_A01Slave


class Contact_A00SlaveSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Contact_A00Slave
        fields = '__all__'


class Contact_A01SlaveSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Contact_A01Slave
        fields = '__all__'


class Contact_A02SlaveSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Contact_A02Slave
        fields = '__all__'


class Group_A00SlaveSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group_A00Slave
        fields = '__all__'


class Group_A01SlaveSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group_A01Slave
        fields = '__all__'
