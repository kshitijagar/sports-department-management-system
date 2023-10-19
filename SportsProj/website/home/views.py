from django.shortcuts import render
from django.shortcuts import redirect

def homeaction(request):
    return render(request,"home.html")
# Create your views here.
