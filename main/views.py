from django.shortcuts import render, redirect

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'main/home.html')


def crisis_support(request):
    return render(request, 'main/crisis_support.html')


def resources(request):
    return render(request, 'main/resources.html')


def privacy_policy(request):
    return render(request, 'main/privacy_policy.html')
