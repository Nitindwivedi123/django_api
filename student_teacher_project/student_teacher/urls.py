from django.urls import path
from .import views

urlpatterns =[
    path('',views.index),
    path('index.html',views.index),
    path('addstudent/',views.StudentInfo),
    path('addteacher/',views.TeacherInfo),
    path('student',views.student),
    path('attendance',views.attendance),
    path('addstudent/student',views.student),
    path('teacher',views.teacher),
    path('addteacher/teacher',views.teacher),
    path('studentattendance/',views.StudentAttendance),
    path('updateinfo/',views.update_info),
]