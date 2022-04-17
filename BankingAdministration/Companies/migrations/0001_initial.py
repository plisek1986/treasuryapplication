# Generated by Django 4.0 on 2022-01-01 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('country', models.CharField(choices=[('Austria', 'AT'), ('Belgium', 'BE'), ('Bulgaria', 'BG'), ('Switzerland', 'CH'), ('Czech Republic', 'CZ'), ('Germany', 'DE'), ('Denmark', 'DK'), ('Estonia', 'EE'), ('Spain', 'ES'), ('Finland', 'FI'), ('France', 'FR'), ('United Kingdom', 'GB'), ('Greece', 'GR'), ('Croatia', 'HR'), ('Hungary', 'HU'), ('Ireland', 'IE'), ('Iceland', 'IS'), ('Italy', 'IT'), ('Kazakhstan', 'KZ'), ('Lithuania', 'LT'), ('Latvia', 'LV'), ('Netherlands', 'NL'), ('Norway', 'NO'), ('Poland', 'PL'), ('Portugal', 'PT'), ('Romania', 'RO'), ('Sweden', 'SE'), ('Slovenia', 'SI'), ('Slovakia', 'SK'), ('Turkey', 'TR')], max_length=64)),
            ],
        ),
    ]