from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Soldier

from django.template import loader

def index(request):
        return HttpResponse("hello world")

def list(request):
        soldiers = Soldier.objects.all()
        soldier_list_template = loader.get_template('intakebook/list.html')
        context = {
                'soldiers' : soldiers
        }
        name_list = ""
        for s in soldiers :
                name_list =  name_list + ", " +s.name
        #return HttpResponse("Soldier List "+name_list)
        return HttpResponse(soldier_list_template.render(context,request))

def detail(request,soldier_id):
        return HttpResponse("Soldier Profile for id  %s " % soldier_id)
