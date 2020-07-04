# Generated by Django 3.0.6 on 2020-06-17 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super', '0002_auto_20200616_0916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='localresident',
            name='location',
        ),
        migrations.RemoveField(
            model_name='organiser',
            name='designation',
        ),
        migrations.AddField(
            model_name='localresident',
            name='pro_pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='organiser',
            name='pro_pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]