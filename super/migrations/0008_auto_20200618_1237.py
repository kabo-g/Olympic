# Generated by Django 3.0.6 on 2020-06-18 12:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('super', '0007_article_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='localresident',
            name='pro_pic',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='organiser',
            name='pro_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]