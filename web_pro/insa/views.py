# -*- coding:utf-8 -*-

from django.shortcuts import render, render_to_response, redirect
from django.http import request, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from insa.models import *
from insa.database.engine import session
from django.template import Context
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

@csrf_exempt
def employee(request):
    rows = session.query(Employee).count()
    print(rows)
    if(rows > 0):
        context_dict = {
            'data': select_all()
        }
        return render(request, 'main.html', context_dict)
    return render(request, 'landing.html')

def counter(request):
    return render_to_response('landing.html')

@csrf_exempt
def count_person(request):
    count = request.POST['emp_count']
    context_dict = {'count': range(0, int(count))}
    return render_to_response('info_input.html',context_dict)


@csrf_exempt
def add_person(request):
    name = request.POST.getlist('name')
    division = request.POST.getlist('division')
    role = request.POST.getlist('role')
    if name and division and role == '':
        return redirect('/')

    else:
        for i in range(0, len(name)):
            emp = Employee(
                name = name[i],
                division = division[i],
                role = role[i]
            )
            session.add(emp)
            session.commit()
        return redirect('/')

def person_main(request, jobID):
    info = session.query(Res).filter_by(emp_id=jobID)
    name = session.query(Employee.name, Employee.id).filter_by(id = jobID)
    context_dict = {
        'data': info,
        'name': name
    }
    return render_to_response('grade.html', context_dict)


def del_info(request, jobID):
    session.query(Employee).filter_by(id=jobID).delete()
    session.commit()
    return redirect('/')
'''
class UserInfo(request):
    def show_grade(self, jobID):
        row = session.query(Employee).filter_by(id=jobID)
        context_dict = {
            'data' : row
        }
        return render_to_response('grade.html',context_dict)
'''
@csrf_exempt
def add_grade(request, jobID):
    user = session.query(Employee).filter_by(id=jobID)
    context_dict = {
        "id" : user
    }
    return render_to_response('subject_num.html', context_dict)

@csrf_exempt
def mark_grade(request, jobID):
    count = request.POST['sub_count']
    context_dict = {'count': range(0, int(count)),
                    'id': jobID}
    return render_to_response('grade_input.html',context_dict)

@csrf_exempt
def input_mark(request, jobID):
    subject = request.POST.getlist('subject')
    course = request.POST.getlist('course')
    mark = request.POST.getlist('mark')
    print(subject)
    print(jobID)
    for i in range(0, len(subject)):
            result = Res(
                emp_id = int(jobID),
                subject = subject[i],
                course = course[i],
                mark = mark[i]
            )
            session.add(result)
            session.commit()
    return redirect('/')

def std_list(request):
    rows = session.query(Standard).count()
    if rows >= 1:
        context_dict = {
            'data': session.query(Standard).all()
        }
        return render_to_response('standard_list.html', context_dict)

    else:

        return render_to_response('std_subject_num.html')
@csrf_exempt
def std_num(request):
    count = request.POST['sub_count']
    context_dict = {'count': range(0, int(count))}
    return render_to_response('standard_input.html', context_dict)

@csrf_exempt
def input_std(request):
    subject = request.POST.getlist('subject')
    course = request.POST.getlist('course')
    mark = request.POST.getlist('stdmark')

    for i in range(0, len(subject)):
            result = Standard(
                subject = subject[i],
                course = course[i],
                standard = mark[i]
            )
            session.add(result)
            session.commit()
    return redirect('view/standard')

def upd_std(request, subject):
    print(subject)
    return redirect('/')
