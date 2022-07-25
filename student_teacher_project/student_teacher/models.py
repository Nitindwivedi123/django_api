from email.policy import default
from django.db import models

# Create your models here.
class student_register(models.Model):
    Id=models.CharField(max_length=20,primary_key=True)
    StudentName=models.CharField(max_length=50,null=True)
    StudentClass=models.CharField(max_length=10,null=True)
    StudentAge=models.PositiveIntegerField()
    StudentGender=models.CharField(max_length=6,null=True)
    StudentJoiningDate=models.DateTimeField(auto_now_add=True)
    Status = models.BooleanField(default=True)

    def __str__(self):
        return self.Id

class teacher_register(models.Model):
    Id=models.CharField(max_length=20,primary_key=True)
    TeacherName=models.CharField(max_length=50,null=True)
    TeacherClass=models.CharField(max_length=10,null=True)
    TeacherJoiningDate=models.DateTimeField(auto_now_add=True)
    Status = models.BooleanField(default=True)
    def __str__(self):
        return self.TeacherName
#
#
class Student_Attendance(models.Model):
    idattendance=models.CharField(max_length=20,primary_key=True)
    #Id=models.CharField(max_length=10,null=True)
    Id=models.ForeignKey(student_register, on_delete=models.CASCADE)
    StudentName=models.CharField(max_length=10,null=True)
    StudentClass=models.CharField(max_length=10,null=True)
    StudentAttendance=models.IntegerField(default=0,null=True)
    date=models.DateField(auto_now_add=True)