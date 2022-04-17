# Generated by Django 4.0 on 2022-04-17 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_auto_20211222_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.CharField(choices=[('treasury', 'Treasury'), ('finance_AP', 'Finance AP'), ('finance_AR', 'Finance AR'), ('finance_GL', 'Finance GL'), ('fp&a', 'FP&A'), ('procurement', 'Procurement')], default='Treasury', max_length=255),
            preserve_default=False,
        ),
    ]