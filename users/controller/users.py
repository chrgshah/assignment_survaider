from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, Http404
from preserialize.serialize import serialize
from django.utils.crypto import get_random_string
from project import settings
from ..models import User
from django.db.models import Count

import traceback
import json
import requests


def index(request):
    return render(request, 'index.html')

def get_records(request):
    try:
        users = User.objects.all()

        if users:
            return JsonResponse({'status': True, 'result': serialize(users)})
        else:
            return JsonResponse({'status': False})

    except Exception as e:
        print e
        return JsonResponse({'status': False})

def get_distribution_gender(request):
    try:
        male_count = User.objects.filter(gender__contains="Male").count()
        female_count = User.objects.filter(gender__contains="Female").count()

        total = male_count + female_count

        data = {}
        data['male'] = round(male_count*100/total)
        data['female'] = round(female_count * 100 / total)
        return JsonResponse({'status': True, 'data':data})

    except Exception as e:
        print e
        return JsonResponse({'status': False})

def get_distribution_relationship(request):
    try:
        relationship1 = User.objects.filter(relationship__contains="Never-married").count()
        relationship2 = User.objects.filter(relationship__contains="Married-civ-spouse").count()
        relationship3 = User.objects.filter(relationship__contains="Divorced").count()
        relationship4 = User.objects.filter(relationship__contains="Married-spouse-absent").count()
        relationship5 = User.objects.filter(relationship__contains="Separated").count()
        relationship6 = User.objects.filter(relationship__contains="Married-AF-spouse").count()

        total =  relationship1 + relationship2 + relationship3 + relationship4 + relationship5 + relationship6
        data = {}
        data['Never_married'] = round(relationship1*100/total)
        data['Married_civ_spouse'] = round(relationship2*100/total)
        data['Divorced'] = round(relationship3*100/total)
        data['Married_spouse_absent'] = round(relationship4*100/total)
        data['Separated'] = round(relationship5*100/total)
        data['Married_AF_spouse'] = round(relationship6*100/total)
        return JsonResponse({'status': True, 'data': data})

    except Exception as e:
        print e
        return JsonResponse({'status': False})
