from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Notice)
admin.site.register(NoticeQuesMod)
admin.site.register(ExamSystem)
admin.site.register(ExamSchedule)
admin.site.register(ThirdExaminerNotice)
admin.site.register(Course)
admin.site.register(InvigilationSchedule)
admin.site.register(ExamResponsibility)
admin.site.register(ExamBill)
admin.site.register(LabCourse)



