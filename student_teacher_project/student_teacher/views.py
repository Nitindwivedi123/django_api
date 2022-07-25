from distutils import errors
from distutils.log import error
from ssl import ALERT_DESCRIPTION_ACCESS_DENIED, AlertDescription
from urllib import response
import json
from django.contrib import messages
from webbrowser import get
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.decorators import api_view
#from rest_framework.serializers import Serializer

from .serializers import student_registerSerializer,teacher_registerSerializer,Student_AttendanceSerializer
from .models import student_register,teacher_register,Student_Attendance

def index(request):
    return render(request,'index.html')

def attendance(request):
   return render(request, "attendance.html")

@api_view(['Post'])
def StudentInfo(request):
    if request.method =="POST":
        msg=''
        data = request.POST
        filter=student_register.objects.filter(Id=data['StudentId'])
        if len(filter):
            return HttpResponse('student already exist.')
            return render(request,'',{"Status":False,"Massege":"Student Id already exist"})
        else:
            user_details= student_register.objects.create(
                Id=data['StudentId'],
                StudentName=data['StudentName'],
                StudentClass=data['StudentClass'],
                StudentAge=data['StudentAge'],
                StudentGender=data['StudentGender']
            )
        #
            return render(request,"index.html")#,{"Status":True,"Massege":"Student successfully added"})

@api_view(['Post'])
def TeacherInfo(request):
    if request.method =="POST":
        data = request.POST
        filter=teacher_register.objects.filter(Id=data['TeacherId'])
        if len(filter):
            return HttpResponse("Teacher exist")
        else:
            user_details= teacher_register.objects.create(
                Id=data['TeacherId'],
                TeacherName=data['TeacherName'],
                TeacherClass=data['TeacherClass']
            )
            return render(request,"index.html")#,{"Status":True,"Massege":"Teacher successfully added"})

@api_view(['POST'])
def StudentAttendance(request): 
    if request.method =="POST":
        data=request.POST
        #StudentClass=data['StudentClass']
        TeacherClass=data['TeacherClass']
        ClassMatch=student_register.objects.all() and student_register.objects.filter(StudentClass=TeacherClass)
        #json_data=json.dump(ClassMatch)
        serializer = student_registerSerializer(ClassMatch,many=True)
        #print("----",str(serializer.data),"----")
        #if len(ClassMatch): 
        return JsonResponse({'profiles':serializer.data},safe=False)
        #return HttpResponse({'Id':ClassMatch})




@api_view(['POST'])
def StudentAttendance1(request):
    #if request.method =="POST":
        #data=request.POST
        data=request.data
        info=teacher_register.objects.filter(TeacherClass=data['TeacherClass'])  
        if len(info):
            ClassMatch=student_register.objects.filter(Id=data['StudentId'],StudentClass=data['TeacherClass'])
            if len(ClassMatch):
                getinfo=student_register.objects.all() and student_register.objects.filter(Id=data['StudentId'])
                if len(getinfo):
                    print(data['StudentId'])
                    student_r =student_register.objects.get(Id=data['StudentId'])
                    #student_n =student_register.objects.get(StudentName=data['StudentName'])

                #print(student_r.__dict__)
                    Student_Attendance.objects.create(
                        idattendance=data['AttendanceId'],
                        Id=student_r,
                        StudentName=student_r.StudentName,
                        StudentClass=data['StudentClass'],
                        StudentAttendance=data['StudentAttendance']
                    )
                    return Response({"Attendance updated"})
                else:
                    return Response({"Student does not exist"})
            else:
                return Response({"Teacher can not take attendance"})

        else:
            return Response({"No Teacher exist"})

def student(request):
   return render(request, "student.html")

def teacher(request):
   return render(request, "teacher.html")

@api_view(['PUT'])
def update_info(request):
    data=request.data
    User=data['User']
    temp=data['UpdateAttribute']
    if User=="teacher":
        update=teacher_register.objects.all() and teacher_register.objects.filter(Id=data['UserId'])
        if len(update):
            if temp=="TeacherName":
                update[0].TeacherFirstName=data[temp]
                for i in update:
                    i.save()
            elif temp=="TeacherClass":
                update[0].TeacherClass=data[temp]
                for i in update:
                    i.save()
            elif temp=="Status":
                update[0].Status=data[temp]
                for i in update:
                    i.save()
            else:
                return Response({"Invalid Input"})
        else:
            return Response({"Teacher does not exit"})
        return Response({"Teacher data updated"})
    elif User=="student":
        update=student_register.objects.all() and student_register.objects.filter(Id=data['UserId'])
        update1=Student_Attendance.objects.filter(Id=data['UserId']) 
        serializer = Student_AttendanceSerializer(update1,many=False)
       

        print("  "+str(update1))
        if len(update):
            if temp=="StudentName":
                update[0].StudentName=data[temp]
                update1[0].StudentName=data[temp] 
                #update1.save()              
                for i in update:
                    i.save()
                for i in update1:
                    i.save()    
                print(" "+str(update1[0].StudentName))
            elif temp=="StudentClass":
                update[0].StudentClass=data[temp]
                for i in update:
                    i.save()
            elif temp=="StudentAge":
                update[0].StudentAge=data[temp]
                for i in update:
                    i.save()
            elif temp=="StudentGender":
                update[0].StudentGender=data[temp]
                for i in update:
                    i.save()
            elif temp=="Status":
                update[0].Status=data[temp]
                for i in update:
                    i.save()
            else:
                return Response({"Invalid Input"})
        else:
            return Response({"Student does not exist"})
        return Response({"Student data updated"})
    elif User=="Attendance":
        update=Student_Attendance.objects.all() and Student_Attendance.objects.filter(Id=data['UserId'])
        if len(update):
            if temp=="StudentAttendance":
                update[0].StudentAttendance=data[temp]
                for i in update:
                    i.save()
            else:
                return Response({"Invalid Input"})
        else:
            return Response({"Student does not exist"})
    else:
        return Response({"User does not exist"})


