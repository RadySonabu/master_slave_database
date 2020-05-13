from django.db import models
from django.db import models
from django.core.validators import RegexValidator
import re

from contact.models import Contact_A00, Contact_A01, Contact_A02, Group_A00, Group_A01


class Contact_A00Slave(models.Model):

    contact_a00_rec = models.ForeignKey(
        Contact_A00, on_delete=models.DO_NOTHING)
    contact_id = models.CharField(max_length=50, default='CON0000000001')
    first_name = models.CharField(max_length=50)
    middle_initial = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address_1 = models.CharField(max_length=50)
    barangay_district = models.CharField(max_length=50)
    city_municipality = models.CharField(max_length=50)
    postal_code = models.IntegerField()
    province = models.CharField(max_length=50)
    phone_1 = models.CharField(validators=[
        RegexValidator(r'^(09|\+639)\d{9}$')], blank=True, max_length=13)  # assuming that the resident is inside the Philippines

    phone_2 = models.CharField(validators=[
        RegexValidator(r'^(09|\+639)\d{9}$')], blank=True, max_length=13)  # assuming that the resident is inside the Philippines

    email = models.EmailField(max_length=254, unique=True)
    status = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.contact_a00_rec} {self.contact_id} {self.first_name} {self.last_name}'


class Contact_A01Slave(models.Model):

    contact_a01_rec = models.ForeignKey(
        Contact_A01, on_delete=models.DO_NOTHING)
    contact_id = models.CharField(max_length=50, default='CON0000000001')
    skill_id = models.IntegerField()
    comments = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.contact_id} {self.skill_id} {self.comments}'


class Contact_A02Slave(models.Model):

    contact_a02_rec = models.ForeignKey(
        Contact_A02, on_delete=models.DO_NOTHING)
    contact_id = models.CharField(max_length=50, default='CON0000000001')
    endorsement_id = models.IntegerField()
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.contact_id} {self.endorsement_id} {self.message}'


class Group_A00Slave(models.Model):
    group_a00_rec = models.ForeignKey(
        Group_A00, on_delete=models.DO_NOTHING)
    group_id = models.CharField(max_length=50, default='GRP0000000001')
    first_name = models.CharField(max_length=50)
    middle_initial = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address_1 = models.CharField(max_length=50)
    barangay_district = models.CharField(max_length=50)
    city_municipality = models.CharField(max_length=50)
    postal_code = models.IntegerField()
    province = models.CharField(max_length=50)
    phone_1 = models.CharField(validators=[
        RegexValidator(r'^(09|\+639)\d{9}$')], blank=True, max_length=13)  # assuming that the resident is inside the Philippines

    phone_2 = models.CharField(validators=[
        RegexValidator(r'^(09|\+639)\d{9}$')], blank=True, max_length=13)  # assuming that the resident is inside the Philippines

    email = models.EmailField(max_length=254, unique=True)
    status = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.group_a00_rec} {self.group_id} {self.first_name} {self.last_name}'


class Group_A01Slave(models.Model):
    group_a01_rec = models.ForeignKey(
        Group_A01, on_delete=models.DO_NOTHING)
    group_id = models.CharField(max_length=50, default='GRP0000000001')
    contact_id = models.CharField(max_length=50, default='CON0000000001')
    group_role = models.CharField(max_length=50)
    comments = models.TextField()
    status = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.group_a01_rec} {self.group_id} {self.contact_id} {self.group_role} {self.comments}'
