# Generated by Django 2.0.3 on 2018-03-20 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kehadiran', '0047_auto_20180320_0153'),
    ]

    operations = [
        migrations.AddField(
            model_name='kehadiran',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]