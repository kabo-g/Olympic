# Generated by Django 3.0.6 on 2020-06-20 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super', '0027_auto_20200620_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('1', 'Available'), ('2', 'Fully Booked')], default='None', max_length=10),
        ),
    ]
