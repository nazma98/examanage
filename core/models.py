from django.db import models
from teachers.models import Staff, Department

# Create your models here.



class ExamSystem(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department')
    semester = models.CharField(max_length=10, blank=True)
    year = models.CharField(max_length=10)

    def __str__(self):
        return self.department.shortcode+' '+self.year+' year '+ self.semester + ' sem'
    

class Notice(models.Model):
    #name = models.CharField(max_length=100)
    memorial_no = models.CharField(max_length=100)
    exam_system = models.ForeignKey(ExamSystem, on_delete=models.CASCADE,  related_name='exam_system_notice')
    exam_year = models.CharField(max_length=4)
    date = models.DateField(auto_now_add=True)
    #fk = models.ForeignKey(Staff, on_delete=models.SET_NULL)

    def __str__(self):
        return 'notice' + self.exam_system.year + ' year '+self.exam_system.semester + ' sem'
    


class NoticeQuesMod(models.Model):
    #staff detail name, dept, university, address
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='staff_ques_mod')
    date = models.DateField()
    day = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    exam_year = models.CharField(max_length=10)
    exam_system = models.ForeignKey(ExamSystem, on_delete=models.CASCADE, related_name='exam_system_ques_mod')


    #committee_member_name = member_name()
    #committee_member_designation = member_designation()
    #committee_member_department = member_department()

    def __str__(self):
        return 'NoticeQuesmod '+self.exam_year+'' + self.exam_system.year +' year '+self.exam_system.semester + ' sem'
    

class Course(models.Model):
    exam_system = models.ForeignKey(ExamSystem, on_delete=models.CASCADE, related_name='exam_system_course')
    course_code = models.CharField(max_length=100)
    course_name = models.CharField(max_length=200)


    def __str__(self):
        return self.course_code
    

class ExamSchedule(models.Model):
    exam_system = models.ForeignKey(ExamSystem, on_delete=models.CASCADE, related_name='exam_system_schedule')
    date_generation = models.DateField(auto_now_add=True)
    exam_year = models.CharField(max_length=10)  
    exam_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_schedule')
    time = models.CharField(max_length=50)
    
    def __str__(self):
        return 'ExamSchedule'+self.exam_year + ' '+ self.exam_system.year+' year '+ self.exam_system.semester+' sem'
    


class InvigilationSchedule(ExamSchedule):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='staff_invigilator')
    
    def __str__(self):
        return 'InvigilationSchedule'+super().exam_year + ' '+ super().exam_system.year+' year '+ super().exam_system.semester+' sem'
    


    
class ThirdExaminerNotice(Notice):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='staff_third_examiner')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_third_examiner')
    examinee_roll_no = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return 'তৃতীয়_পরীক্ষক_নিয়োগ'+self.exam_year + ' '+ self.exam_system.year+' year '+ self.exam_system.semester+' sem'
    



class ExamResponsibility(models.Model):
    exam_year = models.CharField(max_length=20)
    exam_system = models.ForeignKey(ExamSystem, on_delete=models.CASCADE)
    question_no = models.IntegerField()
    notice_ques_mod = models.ForeignKey(NoticeQuesMod, on_delete=models.CASCADE)
    staff_stencil = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='staff_stencil')
    stencil_no = models.IntegerField()
    examinee_no = models.IntegerField()
    lab_exam_invigilator = models.ForeignKey(InvigilationSchedule, on_delete=models.CASCADE)
    examinee_no_viva = models.IntegerField()
    #chairman and members of exam committee in viva voce
    course_lab_tutorial = models.ForeignKey(Course, on_delete=models.CASCADE)
    credit_lab_tutorial = models.IntegerField()
    staff_lab_tutorial = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='staff_lab_tutroial')
    student_no_lab_tutorial = models.IntegerField()


    def __str__(self):
        return 'Exam Responsibility '+ self.exam_system.year+' year '+self.exam_system.semester+' sem'+self.exam_year







    
