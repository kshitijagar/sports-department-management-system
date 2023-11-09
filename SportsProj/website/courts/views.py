from django.shortcuts import render

def courtaction(request):
    srn=request.GET.get('SRN')
    return render(request, 'courts.html',{'SRN': srn})
