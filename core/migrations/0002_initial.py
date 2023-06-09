# Generated by Django 4.2.1 on 2023-05-19 14:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
            name='exam_committee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam_committee', to='core.examcommittee'),
        ),
        migrations.AddField(
            model_name='tabulator',
            name='sem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.semester'),
        ),
        migrations.AddField(
            model_name='tabulator',
            name='tabulator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tabulator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='stencil',
            name='sem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.semester'),
        ),
        migrations.AddField(
            model_name='stencil',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
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
            name='sem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.semester'),
        ),
        migrations.AddField(
            model_name='notice',
            name='sem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.semester'),
        ),
        migrations.AddField(
            model_name='moderationreport',
            name='notice_question_moderation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notice_question_moderation', to='core.noticequestionmoderation'),
        ),
        migrations.AddField(
            model_name='moderationreport',
            name='present_members',
            field=models.ManyToManyField(related_name='present_members', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='labtutorial',
            name='lab_chief',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='labinvigilator',
            name='lab_invigilator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.labcourseschedule'),
        ),
        migrations.AddField(
            model_name='labexaminvigilator',
            name='invigilator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='labexaminvigilator',
            name='lab_course_schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='core.labcourseschedule'),
        ),
        migrations.AddField(
            model_name='labcourseschedule',
            name='invigilator',
            field=models.ManyToManyField(related_name='lab_course_invigilator', through='core.LabExamInvigilator', to=settings.AUTH_USER_MODEL),
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
            name='course_lab_tutorial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_lab_tutorial', to='core.labtutorial'),
        ),
        migrations.AddField(
            model_name='examresponsibility',
            name='exam_committee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.examcommittee'),
        ),
        migrations.AddField(
            model_name='examresponsibility',
            name='moderation_report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.moderationreport'),
        ),
        migrations.AddField(
            model_name='examresponsibility',
            name='sem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.semester'),
        ),
        migrations.AddField(
            model_name='examresponsibility',
            name='staff_stencil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_stencil', to='core.stencil'),
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
            model_name='examcommitteemember',
            name='committee_members',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='committee_members', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='examcommitteemember',
            name='exam_committee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam_committee_for_members', to='core.examcommittee'),
        ),
        migrations.AddField(
            model_name='examcommittee',
            name='exam_committee_member',
            field=models.ManyToManyField(related_name='exam_committee_member', through='core.ExamCommitteeMember', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='examcommittee',
            name='exam_system',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.examsystem'),
        ),
        migrations.AddField(
            model_name='exambill',
            name='exam_responsibility',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam_responsibility', to='core.examresponsibility'),
        ),
        migrations.AddField(
            model_name='exambill',
            name='examiner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='examiner_name', to=settings.AUTH_USER_MODEL),
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
            model_name='labtutorial',
            name='lab_course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.labcourse'),
        ),
        migrations.AddField(
            model_name='labexaminvigilationschedule',
            name='lab_course_schedule',
            field=models.ManyToManyField(through='core.LabCourseSchedule', to='core.labcourse'),
        ),
        migrations.AddField(
            model_name='labcourseschedule',
            name='course_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.labcourse'),
        ),
        migrations.AddField(
            model_name='labcourseschedule',
            name='lab_exam_schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.labexaminvigilationschedule'),
        ),
        migrations.AlterUniqueTogether(
            name='examsystem',
            unique_together={('year', 'year_in_bengali')},
        ),
        migrations.AddField(
            model_name='examresponsibility',
            name='lab_exam_invigilation_schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.labexaminvigilationschedule'),
        ),
        migrations.AlterUniqueTogether(
            name='examiner',
            unique_together={('order', 'examiner')},
        ),
        migrations.AlterUniqueTogether(
            name='examcommittee',
            unique_together={('exam_system', 'exam_year')},
        ),
    ]
