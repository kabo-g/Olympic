# Generated by Django 3.0.6 on 2020-06-20 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super', '0023_auto_20200620_0651'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('1', 'Available'), ('2,', 'Fully Booked')], default='Available', max_length=10),
        ),
    ]
