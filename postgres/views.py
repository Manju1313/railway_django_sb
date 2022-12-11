from django.shortcuts import render,redirect
from django.http import HttpResponse


# Create your views here.
def showmore(request):
    return render(request,"jquery/showmore.html")

def megamenu(request):
    return render(request,"jquery/megamenu.html")

def appendtext(request):
    return render(request,"jquery/addtext.html")

def remove(request):
    return render(request,"jquery/remove.html")

def traversing(request):
    return render(request,"jquery/traversing.html")


def get_post(request):
    return render(request,"jquery/get_post.html") 


def filter(request):
    return render(request,"jquery/filter.html")


def noconflict(request):
    return render(request,"jquery/noconflict.html")


def serilize(request):
    return render(request,"jquery/serilize.html")


def toggle(request):
    return render(request,"jquery/toggle.html")


def proxy(request):
    return render(request,"jquery/proxy.html")


def show_or_hide(request):
    return render(request,"jquery/show_or_hide.html")


def patient_reg(request):
    return render(request,"jquery/patient_reg.html")



# javascript
def output(request):
    return render(request,"javascript/output.html")


def variables(request):
    return render(request,"javascript/variables.html")




