# Generated by Django 4.2.1 on 2023-05-20 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_examsystem_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exambill',
            name='exam_year',
        ),
        migrations.RemoveField(
            model_name='exambill',
            name='sem',
        ),
    ]
