# Generated by Django 5.1.4 on 2024-12-10 14:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_courseschedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseschedule',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.coursetype'),
        ),
    ]
