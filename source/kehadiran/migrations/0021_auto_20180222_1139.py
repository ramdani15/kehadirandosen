# Generated by Django 2.0.2 on 2018-02-22 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kehadiran', '0020_izin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='izin',
            name='dosen',
        ),
        migrations.DeleteModel(
            name='Izin',
        ),
    ]
