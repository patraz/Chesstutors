# Generated by Django 3.2.11 on 2022-01-31 19:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0006_auto_20220131_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='publish',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
