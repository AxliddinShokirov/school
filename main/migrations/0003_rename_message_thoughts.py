# Generated by Django 5.1.4 on 2024-12-09 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_educationstatistics'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Message',
            new_name='Thoughts',
        ),
    ]