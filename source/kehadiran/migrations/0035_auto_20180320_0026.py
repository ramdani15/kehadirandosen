# Generated by Django 2.0.3 on 2018-03-19 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kehadiran', '0034_auto_20180319_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kehadiran',
            name='tanggal',
            field=models.DateField(),
        ),
    ]
