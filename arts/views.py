from django.shortcuts import render
from .models import Arts
# Create your views here.\


def index(request):
    arts = Arts.objects.all()[:10]
    context ={
        'title':'Latest Arts',
        'arts': arts
    }
    return render(request,'arts/index.html',context)
