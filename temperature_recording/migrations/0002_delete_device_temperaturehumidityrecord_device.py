# Generated by Django 4.2.3 on 2023-09-12 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0001_initial'),
        ('temperature_recording', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Device',
        ),
        migrations.AddField(
            model_name='temperaturehumidityrecord',
            name='device',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='device.device'),
            preserve_default=False,
        ),
    ]