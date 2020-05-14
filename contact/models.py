from django.db import models
from django.core.validators import RegexValidator
import re

# individual contact


class Contact_A00(models.Model):

    contact_a00_rec = models.AutoField(primary_key=True)
    contact_id = models.CharField(max_length=50, default='CON0000000000')
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
    status = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.contact_a00_rec} {self.contact_id} {self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        if self._state.adding:

            last_id_raw = Contact_A00.objects.all().aggregate(
                largest=models.Max('contact_id'))['largest']
            if last_id_raw == None:
                last_id_raw = 'CON0000000000'
            else:
                last_id = re.sub('[^0-9]', '', last_id_raw)

                if last_id is not None:
                    if last_id == 0:
                        last_id = 0
                        leading_zero = int(last_id) + 1
                        number_str = str(leading_zero)
                        zero_filled_number = number_str.zfill(10)
                        print(type(zero_filled_number))
                    else:
                        leading_zero = int(last_id) + 1
                        number_str = str(leading_zero)
                        zero_filled_number = number_str.zfill(10)
                        print(type(zero_filled_number))

                    self.contact_id = 'CON' + zero_filled_number
        return super(Contact_A00, self).save(*args, **kwargs)

# individual contact skill and comments


class Contact_A01(models.Model):

    contact_a01_rec = models.AutoField(primary_key=True)
    contact_id = models.ForeignKey(Contact_A00, on_delete=models.DO_NOTHING)
    skill_id = models.IntegerField()
    comments = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.contact_id} {self.skill_id} {self.comments}'


# individual contacts endorsement


class Contact_A02(models.Model):

    contact_a02_rec = models.AutoField(primary_key=True)
    contact_id = models.ForeignKey(Contact_A00, on_delete=models.DO_NOTHING)
    endorsement_id = models.IntegerField()
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.contact_id} {self.endorsement_id} {self.message}'


# group contact


class Group_A00(models.Model):
    group_a00_rec = models.AutoField(primary_key=True)
    group_id = models.CharField(max_length=50, default='GRP0000000000')
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
    status = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.group_a00_rec} {self.group_id} {self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        if self._state.adding:

            last_id_raw = Group_A00.objects.all().aggregate(
                largest=models.Max('group_id'))['largest']
            if last_id_raw == None:
                last_id_raw = 'GRP0000000000'
            else:
                last_id = re.sub('[^0-9]', '', last_id_raw)
                print(type(last_id))
                if last_id is not None:
                    if last_id == 0:
                        last_id = 0
                        leading_zero = int(last_id) + 1
                        number_str = str(leading_zero)
                        zero_filled_number = number_str.zfill(10)
                        print(type(zero_filled_number))
                    else:
                        leading_zero = int(last_id) + 1
                        number_str = str(leading_zero)
                        zero_filled_number = number_str.zfill(10)
                        print(type(zero_filled_number))

                    self.group_id = 'GRP' + zero_filled_number
        return super(Group_A00, self).save(*args, **kwargs)

# group contact with role


class Group_A01(models.Model):
    group_a01_rec = models.AutoField(primary_key=True)
    group_id = models.ForeignKey(Group_A00, on_delete=models.CASCADE)
    contact_id = models.ForeignKey(Contact_A00, on_delete=models.CASCADE)
    group_role = models.CharField(max_length=50)
    comments = models.TextField()
    status = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.group_a01_rec} {self.group_id} {self.contact_id} {self.group_role} {self.comments}'
