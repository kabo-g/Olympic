# Generated by Django 3.0.6 on 2020-06-18 19:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('super', '0011_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue_name', models.CharField(max_length=200, null=True)),
                ('picture', models.ImageField(null=True, upload_to='')),
                ('description', models.CharField(max_length=400, null=True)),
                ('capacity', models.IntegerField(null=True)),
                ('sports', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='super.Sport')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='super.Venue'),
            preserve_default=False,
        ),
    ]