# Generated by Django 2.0.2 on 2018-02-22 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kehadiran', '0014_remove_kehadiran_masuk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kehadiran',
            name='waktu_Mulai',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='kehadiran',
            name='waktu_Selesai',
            field=models.DateTimeField(),
        ),
    ]
