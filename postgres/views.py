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


# Ajax
def ajax_load(request):
    return render(request,"jquery/ajax_load.html")








# javascript
def output(request):
    return render(request,"javascript/output.html")


def operator(request):
    return render(request,"javascript/operator.html")


def variables(request):
    return render(request,"javascript/variables.html")


def function(request):
    return render(request,"javascript/function.html")


def events(request):
    return render(request,"javascript/events.html")


def string(request):
    return render(request,"javascript/string.html")


def stringmethod(request):
    return render(request,"javascript/stringmethod.html")


def search(request):
    return render(request,"javascript/stringsearch.html")


def stringtemplate(request):
    return render(request,"javascript/stringtemplate.html")


def comparison(request):
    return render(request,"javascript/comparison.html")


def ifelse(request):
    return render(request,"javascript/ifelse.html")


def forloop(request):
    return render(request,"javascript/forloop.html")


def whileloop(request):
    return render(request,"javascript/whileloop.html")
