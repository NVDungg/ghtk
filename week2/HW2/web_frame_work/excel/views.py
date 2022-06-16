from django.shortcuts import redirect, render, get_object_or_404
from .models import Student
from .resources import StudentResource
from tablib import Dataset
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
# Create your views here.

def simple_upload(request):
    if request.method == "POST":
        student_resource = StudentResource()
        dataset = Dataset()
        new_student = request.FILES['myfile']

        if not new_student.name.endswith('xlsx'):
            messages.error(request, 'You Must Import Excel File!') #handle the different file
            return redirect("upload")


        imported_data = dataset.load(new_student.read(), format='xlsx')
        for data in imported_data:
            value = Student(
                data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],
                data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19],data[20],
            )

            if Student.objects.filter(student_id=data[3]).exists():
                messages.error(request, 'The Student ID already exists!') #handle the unique id_student
                return redirect("upload")
            else:
                messages.success(request, 'Import Success!')
                value.save()
                return redirect("student-list")
     
    return render(request,'import.html')

def about(request):
    context = {
        'name':'Heloo this it redirect'
    }
    return render(request,'about.html',context)

def search_form(request):
    if request.method == "POST":
        searched_name = request.POST['search_name']
        search_student_id = request.POST['search_student_id']

        name = Student.objects.filter(name__contains=searched_name)
        student_id = Student.objects.filter(student_id__contains=search_student_id)
        combite = Student.objects.filter(
            Q(name__contains = searched_name) &             #This search it combite the name and id_student
            Q(student_id__contains = search_student_id)
        )

        context ={
            "searched_name":searched_name,
            "search_student_id":search_student_id,
            "name":name,
            "student_id":student_id,
            "combite":combite,
            "student_list":Student.objects.all(),
        }
        return render(request, 'search_form.html',context)
    else:
        return render(request, 'search_form.html')


def About(request):
    context={
        'Line_one':"This site make by Python with frame work Django"
    }
    return render(request,'about.html',context)

def detail_student(request, id):
    context = {
        "student_detail":get_object_or_404(Student,pk=id)
    }
    return render(request, 'detail_student.html', context)

def list_student(request):
    context = {
        "student_list":Student.objects.all()
    }
    return render(request, 'Stu_list.html', context)
