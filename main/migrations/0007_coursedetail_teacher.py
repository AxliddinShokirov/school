# Generated by Django 5.1.4 on 2024-12-10 13:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_homework_content_coursedetail_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursedetail',
            name='teacher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.teacher'),
            preserve_default=False,
        ),
    ]
