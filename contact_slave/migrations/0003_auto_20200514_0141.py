# Generated by Django 3.0.6 on 2020-05-13 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0011_auto_20200514_0112'),
        ('contact_slave', '0002_auto_20200514_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_a02slave',
            name='contact_a02_rec',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contact.Contact_A02'),
        ),
    ]