# Generated by Django 4.2.5 on 2023-09-29 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ActivityTrackerApp', '0004_alter_timelog_end_time_alter_timelog_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timelog',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='timelog',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
