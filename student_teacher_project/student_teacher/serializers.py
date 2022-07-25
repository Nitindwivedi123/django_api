from django.db.models import fields
from rest_framework.serializers import ModelSerializer

from .models import student_register,teacher_register,Student_Attendance

class student_registerSerializer(ModelSerializer):
    class Meta:
        model = student_register
        fields = ('Id','StudentName','StudentClass') 

class teacher_registerSerializer(ModelSerializer):
    class Meta:
        model = teacher_register
        fields = ('Id','TeacherName') 

class Student_AttendanceSerializer(ModelSerializer):
    class Meta:
        model = Student_Attendance
        fields = ('Id','StudentName','StudentClass') 

