# -*- coding:utf-8 -*-

from django.shortcuts import render, render_to_response
from django.http import request, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

import json
# Create your views here.

def employee(request):
    return render(request, 'landing.html')

def count_person(request):
    count = request.POST['emp_count']


@csrf_exempt
def add_person(request):
    role = request.POST['role']
    name = request.POST['name']
    div = request.POST['division']


    return HttpResponse(div)
