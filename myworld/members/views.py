import imp
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Members
from django.template import loader
from django.urls import reverse
# Create your views here.


def index(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context,request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({},request))

def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    member = Members(firstname=x,lastname=y)
    member.save()
    return HttpResponseRedirect(reverse('index'))