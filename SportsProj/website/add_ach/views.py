from django.shortcuts import render
import mysql.connector as sql
from django.shortcuts import redirect

cp=''
tit=''
dat=''
pos=''
SRN=''

# Create your views here.
def addachaction(request):
    print('here')
    global cp, tit, SRN, pos, dat
    SRN = request.GET.get('SRN')
    if request.method=="POST":
        print("here also")
        m=sql.connect(host="localhost", user="root", passwd="kshitij2803", database="sports")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="cp":
                cp=value
            if key=="titl":
                tit=value
            if key=="aDate":
                dat=value
            if key=="pos":
                ps=value   
        c="insert into achievements(recorddate, position, awardorg, cashprize, SRN) Values('{}','{}','{}','{}','{}')".format(dat,ps, tit, cp, SRN)
        cursor.execute(c)
        print("here also")
        m.commit()
        return redirect('http://localhost:8000/achievement/?SRN={}'.format(SRN))
    return render(request, 'add_achievement.html',{'SRN':SRN})