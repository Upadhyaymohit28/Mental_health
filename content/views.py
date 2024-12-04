from django.shortcuts import render
from .models import EducationalContent
import random


def list_content(request):
  
    contents = EducationalContent.objects.all().order_by('-created_at')
    return render(request, 'content/list_content.html', {'contents': contents})