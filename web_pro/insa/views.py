# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import request, HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json
# Create your views here.

def employee(request):
    return render(request, 'landing.html')

@csrf_exempt
def add_person(request):
    data = request.body
    print (data.decode('euc-kr'))
    return HttpResponse(data)
