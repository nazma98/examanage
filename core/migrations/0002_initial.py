# Generated by Django 4.2.1 on 2023-05-13 14:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thirdexaminer',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tabulator',
            name='tabulator',
            field=models.ForeignKey(limit_choices_to={'role': 'member'}, on_delete=django.db.models.deletion.CASCADE, to='core.examcommittee'),
        ),
        migrations.AddField(
            model_name='stencil',
            name='exam_responsibility',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.examresponsibility'),
        ),
        migrations.AddField(
            model_name='stencil',
            name='staff',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='semester',
            name='exam_system',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.examsystem'),
        ),
        migrations.AddField(
            model_name='noticequestionmoderation',
            name='exam_committee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.examcommittee'),
        ),
        migrations.AddField(
            model_name='noticequestionmoderation',
            name='external_examiner',
            field=models.OneToOneField(limit_choices_to={'is_external': True}, on_delete=django.db.models.deletion.CASCADE, related_name='external_examiner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='noticequestionmoderation',
            name='sem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.semester'),
        ),
        migrations.AddField(
            model_name='notice',
            name='sem',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.semester'),
        ),
        migrations.AddField(
            model_name='moderationreport',
            name='notice_question_moderation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.noticequestionmoderation'),
        ),
        migrations.AddField(
            model_name='moderationreport',
            name='present_members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='invigilator',
            name='course_schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='core.courseschedule'),
        ),
        migrations.AddField(
            model_name='invigilator',
            name='invigilator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='examsystem',
            name='committee_members',
            field=models.ManyToManyField(related_name='committee_member', through='core.ExamCommittee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='examsystem',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department', to='teachers.department', to_field='shortcode'),
        ),
        migrations.AddField(
            model_name='examschedule',
            name='course_schedule',
            field=models.ManyToManyField(through='core.CourseSchedule', to='core.course'),
        ),
        migrations.AddField(
            model_name='examschedule',
            name='sem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.semester'),
        ),
        migrations.AddField(
            model_name='examresponsibility',
            name='sem',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.semester'),
        ),
        migrations.AddField(
            model_name='examresponsibility',
            name='staff_lab_tutorial',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='examresponsibility',
            name='staff_stencil',
            field=models.ManyToManyField(related_name='staff_stencil', through='core.Stencil', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='examresponsibility',
            name='tabulators',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tabulators', to='core.tabulator'),
        ),
        migrations.AddField(
            model_name='examinerlist',
            name='course',
            field=models.ManyToManyField(related_name='course_examiner_list', through='core.CourseExaminer', to='core.course'),
        ),
        migrations.AddField(
            model_name='examinerlist',
            name='sem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.semester'),
        ),
        migrations.AddField(
            model_name='examiner',
            name='course_examiner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.courseexaminer'),
        ),
        migrations.AddField(
            model_name='examiner',
            name='examiner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='examcommittee',
            name='exam_system',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.examsystem'),
        ),
        migrations.AddField(
            model_name='examcommittee',
            name='staff_member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='exambill',
            name='chairman',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='exam_committee_chairman', to='core.examcommittee'),
        ),
        migrations.AddField(
            model_name='exambill',
            name='exam_responsibility',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam_responsibility', to='core.examresponsibility'),
        ),
        migrations.AddField(
            model_name='exambill',
            name='examiner_bangla',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='examiner_bangla', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='exambill',
            name='examiner_english',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='examiner_english', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='exambill',
            name='sem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sem', to='core.semester'),
        ),
        migrations.AddField(
            model_name='courseschedule',
            name='course_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.course'),
        ),
        migrations.AddField(
            model_name='courseschedule',
            name='exam_schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.examschedule'),
        ),
        migrations.AddField(
            model_name='courseschedule',
            name='invigilator',
            field=models.ManyToManyField(related_name='course_invigilator', through='core.Invigilator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='courseexaminer',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.course'),
        ),
        migrations.AddField(
            model_name='courseexaminer',
            name='examiner_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.examinerlist'),
        ),
        migrations.AddField(
            model_name='courseexaminer',
            name='examiners',
            field=models.ManyToManyField(related_name='examiners', through='core.Examiner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semester_course', to='core.semester'),
        ),
        migrations.AddField(
            model_name='thirdexaminernotice',
            name='examiner',
            field=models.ManyToManyField(related_name='third_examiner', through='core.ThirdExaminer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='thirdexaminer',
            name='notice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.thirdexaminernotice'),
        ),
        migrations.AlterUniqueTogether(
            name='semester',
            unique_together={('exam_system', 'semester')},
        ),
        migrations.AddField(
            model_name='examresponsibility',
            name='course_lab_tutorial',
            field=models.ManyToManyField(related_name='course_lab_tutorial', to='core.labcourse'),
        ),
        migrations.AlterUniqueTogether(
            name='examiner',
            unique_together={('order', 'examiner')},
        ),
        migrations.AlterUniqueTogether(
            name='examcommittee',
            unique_together={('exam_system', 'staff_member', 'exam_year')},
        ),
    ]
