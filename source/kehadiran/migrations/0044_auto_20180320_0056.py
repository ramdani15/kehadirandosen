# Generated by Django 2.0.3 on 2018-03-19 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kehadiran', '0043_auto_20180320_0055'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kehadiran',
            options={'ordering': ['dosen', 'tanggal']},
        ),
    ]