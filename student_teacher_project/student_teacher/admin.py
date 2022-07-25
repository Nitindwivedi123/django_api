
from django.contrib import admin
from .models import student_register,teacher_register,Student_Attendance
# Register your models here.

class student_registerAdmin(admin.ModelAdmin):
    list_display = ('Id','StudentName','StudentClass','StudentAge','StudentGender','StudentJoiningDate','Status')
admin.site.register(student_register,student_registerAdmin)

class teacher_registerAdmin(admin.ModelAdmin):
    list_display = ('Id','TeacherName','TeacherClass','TeacherJoiningDate','Status')
admin.site.register(teacher_register,teacher_registerAdmin)

class Student_AttendanceAdmin(admin.ModelAdmin):
    list_display = ('idattendance','Id','StudentName','StudentClass','StudentAttendance','date')
admin.site.register(Student_Attendance,Student_AttendanceAdmin)

