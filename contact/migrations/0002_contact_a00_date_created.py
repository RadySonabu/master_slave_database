# Generated by Django 3.0.6 on 2020-05-13 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_a00',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
