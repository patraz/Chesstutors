# Generated by Django 3.2.11 on 2022-01-30 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0002_alter_avaliability_announcement'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
            preserve_default=False,
        ),
    ]
