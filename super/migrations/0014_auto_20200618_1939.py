# Generated by Django 3.0.6 on 2020-06-18 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('super', '0013_auto_20200618_1938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venue',
            name='sports',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='Venue',
        ),
    ]
