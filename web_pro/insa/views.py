# -*- coding:utf-8 -*-

from django.shortcuts import render, render_to_response, redirect
from django.http import request, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from insa.models import Employee
from insa.database.engine import session
from insa.utils.encoder import AlchemyEncoder

import json
# Create your views here.

def select_all():
    queries = session.query(Employee).all
    return queries

def main_redirect():
    context_dict = {
            'data': select_all()
        }
    return render(request, 'main.html', context_dict)

def employee(request):
    rows = session.query(Employee).count()
    if(rows > 0):
        context_dict = {
            'data': select_all()
        }
        return render(request, 'main.html', context_dict)
    return render(request, 'landing.html')


def count_person(request):
    count = request.POST['emp_count']
    context_dict = {'count': range(0, int(count))}
    return render_to_response('info_input.html',context_dict)


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

    queries = session.query(Employee).all
    #raw = [dict(name = r.name, division = r.division, role = r.role)for r in queries]
    #딕셔너리 인 리스트 타입 익스팬드 필요.



    context_dict = {
                        'data': queries
                    }
    return render_to_response('main.html', context_dict)


def person_main(request):

    return redirect('')

def del_info(request, jobID):
    session.query(Employee).filter_by(id=jobID).delete()
    session.commit()
    context_dict = {
            'data': select_all()
        }
    return render(request, 'main.html', context_dict)

class UserInfo(request):
    def show_grade(self, jobID):
        row = session.query(Employee).filter_by(id=jobID)
        context_dict = {
            'data' : row
        }
        return render_to_response('grade.html',context_dict)
