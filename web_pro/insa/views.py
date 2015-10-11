# -*- coding:utf-8 -*-

from django.shortcuts import render, render_to_response, redirect
from django.http import request, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from insa.models import Employee
from insa.database.engine import session
from insa.utils.encoder import AlchemyEncoder

import json
# Create your views here.

def employee(request):
    query = session.query(Employee)
    data = [dict(id=q.id)for q in query]
    if(len(data) == 0 or len(data) < 0):
        return render(request, 'landing.html')
    else:
        return render(request, 'main.html')


def count_person(request):
    count = request.POST['emp_count']
    context_dict = {'count': range(0, int(count))}
    return render(request, 'info_input.html',context_dict)


@csrf_exempt
def add_person(request):
    name = request.POST.getlist('name')
    division = request.POST.getlist('division')
    role = request.POST.getlist('role')


    for i in range(0, len(name)):
        emp = Employee(
            name = name[i],
            division = division[i],
            role = role[i]
        )
        l = session.add(emp)
        session.commit()
    print ('aft query')

    queries = session.query(Employee)
    raw = [dict(name = r.name, division = r.division, role = r.role)for r in queries]
    print(raw)


    context_dict = {
                        'data': data
                    }
    return render(request, 'main.html', context_dict)


def person_main(request):

    return redirect('')
