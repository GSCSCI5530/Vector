# Generated by Django 2.1.2 on 2018-11-05 02:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('eventmanager', '0005_remove_attendee_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='user_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
