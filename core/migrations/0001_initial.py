# Generated by Django 4.2.1 on 2023-05-14 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=100, unique=True)),
                ('course_name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseExaminer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_marks', models.IntegerField()),
                ('duration', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CourseSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_date', models.DateField()),
                ('time', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ExamBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_year', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ExamCommittee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_year', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ExamCommitteeMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('chairman', 'Chairman'), ('member', 'Member'), ('external', 'External')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Examiner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='ExaminerList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_year', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='ExamResponsibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_year', models.CharField(max_length=20)),
                ('question_no', models.IntegerField()),
                ('examinee_no_viva', models.IntegerField()),
                ('student_no_lab_tutorial', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ExamSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_generation', models.DateField(auto_now_add=True)),
                ('exam_year', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ExamSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th')], max_length=10)),
                ('year_in_bengali', models.CharField(choices=[('১ম', '১ম'), ('২য়', '২য়'), ('৩য়', '৩য়'), ('৪র্থ', '৪র্থ')], max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Invigilator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='LabCourseSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_date', models.DateField()),
                ('time', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LabExamInvigilator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ModerationReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memorial_no', models.CharField(max_length=100)),
                ('exam_year', models.CharField(max_length=4)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='NoticeQuestionModeration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('day', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=20)),
                ('exam_year', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(choices=[('1st', '1st'), ('2nd', '2nd')], max_length=5)),
                ('semester_in_bengali', models.CharField(choices=[('১ম', '১ম'), ('২য়', '২য়')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Stencil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stencil_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tabulator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examinee_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LabCourse',
            fields=[
                ('course_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.course')),
                ('credit', models.IntegerField()),
            ],
            bases=('core.course',),
        ),
        migrations.CreateModel(
            name='LabExamInvigilationSchedule',
            fields=[
                ('examschedule_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.examschedule')),
                ('roll_type', models.CharField(choices=[('O', 'Odd Roll'), ('E', 'Even Roll')], max_length=1)),
            ],
            bases=('core.examschedule',),
        ),
        migrations.CreateModel(
            name='ThirdExaminerNotice',
            fields=[
                ('notice_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.notice')),
            ],
            bases=('core.notice',),
        ),
        migrations.CreateModel(
            name='ThirdExaminer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examinee_roll', models.CharField(blank=True, max_length=500)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.course')),
            ],
        ),
    ]
