# Generated by Django 3.0.6 on 2020-05-13 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0009_auto_20200514_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_a00',
            name='contact_id',
            field=models.CharField(default='CON0000000000', max_length=50),
        ),
        migrations.AlterField(
            model_name='contact_a01',
            name='contact_id',
            field=models.CharField(default='CON0000000000', max_length=50),
        ),
        migrations.AlterField(
            model_name='contact_a02',
            name='contact_id',
            field=models.CharField(default='CON0000000000', max_length=50),
        ),
        migrations.AlterField(
            model_name='group_a00',
            name='group_id',
            field=models.CharField(default='GRP0000000000', max_length=50),
        ),
        migrations.AlterField(
            model_name='group_a01',
            name='contact_id',
            field=models.CharField(default='CON0000000000', max_length=50),
        ),
        migrations.AlterField(
            model_name='group_a01',
            name='group_id',
            field=models.CharField(default='GRP0000000000', max_length=50),
        ),
    ]
