# Generated by Django 3.0.6 on 2020-06-20 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super', '0029_auto_20200620_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('available', 'Available'), ('booked', 'Fully Booked')], default='None', max_length=10),
        ),
    ]