from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from stu.models import Student


def index_view(request):

    return render(request, 'login.html')


def login_view(request):  #登录功能
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        uname = request.POST.get('uname', '')
        pwd = request.POST.get('pwd', '')
        if uname and pwd:
            student = Student(sname=uname, spwd=pwd)
            student.save()
            return HttpResponse('ok')
    return HttpResponse('NO')


def shwo_view(request):
    stus = Student.objects.all()

    return render(request, 'show.html', {'s': stus})


def reg_view(request):
    if request.method == 'GET':
        return render(request, 'red.html')
    else:
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        if uname and pwd:
            c = Student.objects.filter(sname=uname, spwd=pwd).count()
            #获取里面的记录  count()
            if c == 1:
                return HttpResponse('OK登录')
    return HttpResponse('NO登录失败')


def mov_view(request):

    return render(request, 'mov.html')

    pass