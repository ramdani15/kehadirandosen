# Generated by Django 2.0.2 on 2018-03-01 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kehadiran', '0024_auto_20180301_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kehadiran',
            name='jenis_kehadiran',
            field=models.CharField(choices=[('sibuk', 'Sibuk'), ('senggang', 'Senggang'), ('tidakmasuk', 'Tidak Masuk'), ('ttd', 'TTD')], max_length=20),
        ),
    ]
