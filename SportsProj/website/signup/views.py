from django.shortcuts import render
import mysql.connector as sql
from django.shortcuts import redirect

fn=''
ln=''
s=''
em=''
pwd=''

# Create your views here.
def signaction(request):
    global fn,ln,s,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost", user="root", passwd="JugguSQL@123", database="sports")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="name":
                n=value
            if key=="SRN":
                SRN=value
            if key=="sex":
                s=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value   
            if key=="mobile":
                mob=value  
            if key=="bg":
                bg=value 
        c="insert into student Values('{}','{}','{}','{}','{}', '{}', '{}')".format(SRN,n,mob, em, bg, pwd, s)
        cursor.execute(c)
        m.commit()
        return redirect('http://localhost:8000/login/')
    return render(request, 'signup_page.html')