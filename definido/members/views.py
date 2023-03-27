from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Table1

def hello(request):
    return HttpResponse('<center><h1> funciona logo disgraça </h1></center>')
# Create your views here.
def name (request , name):
    return render(request , 'name.html',{'name':name})

def members(request):
    mymembers = Table1.objects.all().values()
    tittle = Table1
    template = loader.get_template('member.html')
    context={
        'mymembers':mymembers
    }
    return HttpResponse(template.render(context,request))
def exercise (request):
    template = loader.get_template('exercise.html')
    return HttpResponse(template.render({},request))