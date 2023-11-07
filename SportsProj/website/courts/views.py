from django.shortcuts import render

def courtaction(request):
    #m = sql.connect(host="localhost", user="root", passwd="kshitij2803", database="sports")
    #cursor = m.cursor()
    
    srn = request.GET.get('SRN')
    print(srn)
    return render(request,'courts.html',{'SRN': srn})
