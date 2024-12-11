# Generated by Django 5.1.4 on 2024-12-10 15:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_courseschedule_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursedetail',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coursedetail',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_details', to='main.course'),
        ),
        migrations.AlterField(
            model_name='coursedetail',
            name='izox',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.coursetype'),
        ),
        migrations.AlterField(
            model_name='courseschedule',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.coursetype'),
        ),
        migrations.AlterField(
            model_name='courseschedule',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.teacher'),
        ),
    ]