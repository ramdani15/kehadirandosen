# Generated by Django 2.0.2 on 2018-02-22 08:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kehadiran', '0011_auto_20180222_0809'),
    ]

    operations = [
        migrations.AddField(
            model_name='kehadiran',
            name='waktu',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
