# Generated by Django 4.2.1 on 2023-09-11 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='installation_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]