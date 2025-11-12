from django.shortcuts import render
from django.views.generic import View
from student.models import StudentModel

# Create your views here.

#create view

class CreatestudentView(View):

    def get(self,request):

        return render(request,"add_student.html")

    def post(self,request):

        print(request.POST)

        StudentModel.objects.create(name = request.POST.get('studentname'),
                                    roll_no = request.POST.get('studentroll'),
                                    department = request.POST.get('studentdepartment'),
                                    email = request.POST.get('studentemail'),
                                    marks = request.POST.get('studentmarks'))

        return render(request,"add_student.html")


# read view

class ReadstudentView(View):

    def get(self,request):

        data = StudentModel.objects.all()

        return render(request,"read_student.html",{"data":data})


# update view

class StudentupdateView(View):

    def get(self,request,**kwargs):

        update_id = kwargs.get("pk")

        student_data = StudentModel.objects.get(id=update_id)

        return render(request,"update_student.html",{"student_data":student_data})

    def post(self,request,**kwargs):

        update_id = kwargs.get("pk")

        student_data = StudentModel.objects.get(id=update_id)

        print(request.POST)

        student_data.name = request.POST.get("studentname")

        student_data.roll_no = request.POST.get("studentroll")

        student_data.department = request.POST.get("studentdepartment")

        student_data.email = request.POST.get("studentemail")

        student_data.marks = request.POST.get("studentmarks")

        student_data.save()

        return render(request,"update_student.html")


# delete view

class DeletestudentView(View):

    def get(self,request):

        student_data = StudentModel.objects.get(id=3)

        student_data.delete()

        return render(request,"add_student.html")


# retreive view

class RetreivestudentView(View):

    def get(self,request,**kwargs):

        retreive_id = kwargs.get("pk")

        student_data = StudentModel.objects.get(id = retreive_id)

        return render(request,"retreive_student.html",{"student_data":student_data})