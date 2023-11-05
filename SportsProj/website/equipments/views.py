from django.shortcuts import render

def equipaction(request):
    srn = request.GET.get('SRN')
    return render(request, 'equipments.html')