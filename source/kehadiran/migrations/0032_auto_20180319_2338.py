# Generated by Django 2.0.3 on 2018-03-19 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kehadiran', '0031_kehadiran_tanggal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kehadiran',
            name='tanggal',
            field=models.DateField(verbose_name='timezone.now'),
        ),
    ]
