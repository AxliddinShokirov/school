# Generated by Django 5.1.4 on 2024-12-10 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_coursedetail_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursedetail',
            name='teacher',
        ),
    ]
