# Generated by Django 2.2.4 on 2019-11-10 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idform',
            name='resident_idform',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='residents.Resident'),
        ),
    ]
