from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member

# Create your views here.
def index(request):
    # template = loader.get_template("dkcoder.html")
    # return HttpResponse(template.render())
    mymember = Member.objects.all().values()
    # output = ""
    # for x in mymember:
    #     output += x["firstname"]
    # return HttpResponse(output)
    mymember = Member.objects.all().values()
    template = loader.get_template("dkcoder.html")
    context = {
        'mymember':mymember,
    }
    return HttpResponse(template.render(context,request))

def add(request):
    template = loader.get_template("add.html")
    return HttpResponse(template.render({},request))

def addrecord(request):
    x = request.POST['fnm']
    y = request.POST['lnm']

    member = Member(firstname=x, lastname=y)
    member.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    dkmember = Member.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'dkmember':dkmember,
    }
    return HttpResponse(template.render(context,request))

def updaterecord(request, id):
    x= request.POST['fnm1']
    y = request.POST['lnm1']

    member = Member.objects.get(id=id)
    member.firstname = x
    member.lastname = y
    member.save()
    return HttpResponseRedirect(reverse('index'))