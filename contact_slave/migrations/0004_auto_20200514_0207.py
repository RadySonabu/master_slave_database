# Generated by Django 3.0.6 on 2020-05-13 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_slave', '0003_auto_20200514_0141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group_a01slave',
            old_name='Group_A01_Rec',
            new_name='group_a01_rec',
        ),
    ]