# Generated by Django 4.2.1 on 2023-05-19 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
        ('core', '0002_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='examsystem',
            unique_together={('department', 'year', 'year_in_bengali')},
        ),
    ]
