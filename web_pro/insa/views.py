# -*- coding:utf-8 -*-

from django.shortcuts import render, render_to_response, redirect
from django.http import request, HttpResponse
from django.views.decorators.csrf import csrf_exempt

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
    name_list = []
    role_list = []
    div_list = []
    for i in range(0, len(name)):
        name_list.append(name[i])
        role_list.append(role[i])
        div_list.append(division[i])

    context_dict = {'name': name_list,
                    'role': role_list,
                    'division': div_list,
                    'range': range(0, len(name))}
    print (context_dict)
    return render(request, 'main.html', context_dict)


def person_main(request):
    pass
