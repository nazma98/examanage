# Generated by Django 4.2.1 on 2023-05-23 10:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_remove_exambill_exam_year_remove_exambill_sem'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabCourseChief',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_no', models.IntegerField()),
                ('lab_chief', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('lab_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.labcourse')),
            ],
        ),
        migrations.CreateModel(
            name='LabTutorialList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_year', models.CharField(max_length=4)),
                ('lab_course_info', models.ManyToManyField(related_name='lab_course_chief', through='core.LabCourseChief', to='core.labcourse')),
                ('sem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.semester')),
            ],
        ),
        migrations.AddField(
            model_name='labcoursechief',
            name='lab_tutorial_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.labtutoriallist'),
        ),
    ]
