from django.shortcuts import render, get_object_or_404
from .models import EducationalContent

def list_content(request):
    contents = EducationalContent.objects.all().order_by('-created_at')
    return render(request, 'content/list_content.html', {'contents': contents})

def content_detail(request, content_id):
    content = get_object_or_404(EducationalContent, id=content_id)
    return render(request, 'content/content_detail.html', {'content': content})