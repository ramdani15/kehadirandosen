# Generated by Django 2.0.2 on 2018-02-21 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kehadiran', '0002_auto_20180221_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kehadiran',
            name='waktu',
            field=models.TimeField(blank=True),
        ),
    ]