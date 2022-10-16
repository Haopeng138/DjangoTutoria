from django.shortcuts import render
from django.http import HttpResponse
from .models import Members
from django.template import loader
# Create your views here.


def index(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context,request))