# Generated by Django 3.2.11 on 2022-02-21 18:49

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0012_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='phone_number',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]
