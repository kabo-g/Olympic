# Generated by Django 3.0.6 on 2020-06-18 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('super', '0016_delete_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('picture', models.ImageField(null=True, upload_to='')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField()),
                ('description', models.CharField(max_length=255)),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='super.Sport')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='super.Venue')),
            ],
        ),
    ]
