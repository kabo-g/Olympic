# Generated by Django 3.0.6 on 2020-06-21 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super', '0036_remove_venue_sports'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_localresident',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_organiser',
            field=models.BooleanField(null=True),
        ),
    ]
