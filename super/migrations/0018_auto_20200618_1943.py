# Generated by Django 3.0.6 on 2020-06-18 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super', '0017_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='capacity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
