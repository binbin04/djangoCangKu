
from django.shortcuts import render, HttpResponse, redirect

from student.models import *

# Create your views here.


def student_list(request):
    if request.method == "GET":
        info = Student.objects.all()
        return render(request, "student_list.html", {"info": info})


def student_add(request):
    if request.method == "GET":
        return render(request, "student_add.html")
    name = request.POST.get("name")
    age = request.POST.get("age")
    gender = request.POST.get("gender")
    phone = request.POST.get("phone")
    Student.objects.create(name=name, age=age, gender=gender, phone=phone)
    return redirect("/students/")


def student_delete(request, sid=None):
    if request.method == "GET":
        if sid is not None:
            Student.objects.filter(id=sid).delete()
            return redirect("/students/")
        return render(request, "student_delete.html")
    try:
        name = request.POST.get("name")
        Student.objects.filter(name=name).delete()
        return redirect("/students/")
    except:
        return redirect("/students/")


def student_query(request):
    if request.method == "GET":
        try:
            name = request.GET.get("name")
            info = Student.objects.filter(name=name).all()
            return render(request, "student_query.html", {"info": info})
        except:
            return render(request, "student_query.html")


def student_edit(request, sid):
    if request.method == "GET":
        info = Student.objects.get(id=sid)
        return render(request, "student_edit.html", {"info": info})
    name = request.POST.get("name")
    age = request.POST.get("age")
    gender = request.POST.get("gender")
    phone = request.POST.get("phone")
    Student.objects.filter(id=sid).update(name=name, age=age, gender=gender, phone=phone)
    return redirect("/students/")


def depart_list(request):
    """部门列表"""
    # 去数据库中获取部门信息
    info = Department.objects.all()
    return render(request, "depart_list.html", {"info": info})

