# Generated by Django 2.0.2 on 2018-02-21 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kehadiran', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kehadiran',
            old_name='profil',
            new_name='dosen',
        ),
    ]