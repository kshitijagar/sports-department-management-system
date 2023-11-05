from django.shortcuts import render
from django.shortcuts import redirect

def homeaction(request):
    srn = request.GET.get('SRN')
    return render(request,"home.html", {'SRN': srn})
# Create your views here.
