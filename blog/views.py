from django.shortcuts import render

# Create your views here.
def ajax_state(request):
    return render(request,"state_dist/ajax.html")


