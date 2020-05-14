# Generated by Django 2.2.10 on 2020-05-14 12:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_A00',
            fields=[
                ('contact_a00_rec', models.AutoField(primary_key=True, serialize=False)),
                ('contact_id', models.CharField(default='CON0000000000', max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_initial', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address_1', models.CharField(max_length=50)),
                ('barangay_district', models.CharField(max_length=50)),
                ('city_municipality', models.CharField(max_length=50)),
                ('postal_code', models.IntegerField()),
                ('province', models.CharField(max_length=50)),
                ('phone_1', models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator('^(09|\\+639)\\d{9}$')])),
                ('phone_2', models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator('^(09|\\+639)\\d{9}$')])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('status', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group_A00',
            fields=[
                ('group_a00_rec', models.AutoField(primary_key=True, serialize=False)),
                ('group_id', models.CharField(default='GRP0000000000', max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_initial', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address_1', models.CharField(max_length=50)),
                ('barangay_district', models.CharField(max_length=50)),
                ('city_municipality', models.CharField(max_length=50)),
                ('postal_code', models.IntegerField()),
                ('province', models.CharField(max_length=50)),
                ('phone_1', models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator('^(09|\\+639)\\d{9}$')])),
                ('phone_2', models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator('^(09|\\+639)\\d{9}$')])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('status', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group_A01',
            fields=[
                ('group_a01_rec', models.AutoField(primary_key=True, serialize=False)),
                ('group_role', models.CharField(max_length=50)),
                ('comments', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('contact_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.Contact_A00')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.Group_A00')),
            ],
        ),
        migrations.CreateModel(
            name='Contact_A02',
            fields=[
                ('contact_a02_rec', models.AutoField(primary_key=True, serialize=False)),
                ('endorsement_id', models.IntegerField()),
                ('message', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('contact_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contact.Contact_A00')),
            ],
        ),
        migrations.CreateModel(
            name='Contact_A01',
            fields=[
                ('contact_a01_rec', models.AutoField(primary_key=True, serialize=False)),
                ('skill_id', models.IntegerField()),
                ('comments', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('contact_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contact.Contact_A00')),
            ],
        ),
    ]
