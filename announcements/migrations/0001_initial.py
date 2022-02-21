# Generated by Django 3.2.11 on 2022-02-21 19:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('publish', models.DateField(auto_now=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('currency', models.CharField(choices=[('PLN', 'PLN'), ('USD', 'USD'), ('NOK', 'NOK'), ('RUB', 'RUB'), ('EUR', 'EUR')], max_length=3)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500)),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('publish', models.DateTimeField(auto_now_add=True)),
                ('announcement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='announcements.announcement')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Avaliability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Poniedziałek', 'Poniedziałek'), ('Wtorek', 'Wtorek'), ('Środa', 'Środa'), ('Czwartek', 'Czwartek'), ('Piątek', 'Piątek'), ('Sobota', 'Sobota'), ('Niedziela', 'Niedziela')], max_length=12)),
                ('av_from', models.TimeField(blank=True, null=True)),
                ('av_to', models.TimeField(blank=True, null=True)),
                ('announcement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avs', to='announcements.announcement')),
            ],
        ),
    ]
