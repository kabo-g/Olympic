# Generated by Django 3.0.6 on 2020-06-16 09:16

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('super', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='localresident',
            name='id',
        ),
        migrations.RemoveField(
            model_name='localresident',
            name='password1',
        ),
        migrations.RemoveField(
            model_name='localresident',
            name='password2',
        ),
        migrations.RemoveField(
            model_name='organiser',
            name='id',
        ),
        migrations.RemoveField(
            model_name='organiser',
            name='password1',
        ),
        migrations.RemoveField(
            model_name='organiser',
            name='password2',
        ),
        migrations.RemoveField(
            model_name='user',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='user',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='user',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='pro_pic',
        ),
        migrations.AddField(
            model_name='localresident',
            name='location',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='localresident',
            name='phone_number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='organiser',
            name='designation',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='organiser',
            name='phone_number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='localresident',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='organiser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_localresident',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_organiser',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
        migrations.AlterModelTable(
            name='organiser',
            table=None,
        ),
    ]