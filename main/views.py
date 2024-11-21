from django.shortcuts import render, redirect


def home(request):
    return render(request, 'main/home.html')


def crisis_support(request):
    return render(request, 'main/crisis_support.html')


def resources(request):
    return render(request, 'main/resources.html')
