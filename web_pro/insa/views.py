# -*- coding:utf-8 -*-

from django.shortcuts import render, render_to_response, redirect
from django.http import request, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from insa.models import Employee
from insa.database.engine import session

import json
# Create your views here.

def employee(request):
    return render(request, 'landing.html')

def count_person(request):
    count = request.POST['emp_count']
    context_dict = {'count': range(0, int(count))}
    return render(request, 'info_input.html',context_dict)


@csrf_exempt
def add_person(request):
    name = request.POST.getlist('name')
    division = request.POST.getlist('division')
    role = request.POST.getlist('role')

    data = zip(name, role, division)
    for i in range(0, len(name)):
        emp = Employee(
            name = name[i],
            division = 1,
            role = 1
        )
        l = session.add(emp)
        print(l)


    context_dict = {
                        'data': data
                    }
    print(context_dict)
    return render(request, 'main.html', context_dict)


def person_main(request):

    return redirect('')
