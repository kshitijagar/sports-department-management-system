
from django.shortcuts import render, redirect
import mysql.connector as sql

def loginaction(request):
    global em, pwd
    error_message = ''  # Initialize error_message here

    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="kshitij2803", database="sports")
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "email":
                em = value
            if key == "password":
                pwd = value

        c = "select * from student where emailid='{}' and password='{}'".format(em, pwd)
        cursor.execute(c)
        
        t = tuple(cursor.fetchall())
        d = "select * from student where SRN='{}' and password='{}'".format(em, pwd)
        cursor.execute(d)
        
        k = tuple(cursor.fetchall())
        
        if t != () or k != ():
            if t:
                u="select SRN from student where emailid='{}'".format(em)
                cursor.execute(u)
                SRN= str(cursor.fetchall()[0])
                SRN=SRN[2:-3]
                print(SRN)
                return redirect("http://localhost:8000/home/?SRN={}".format(SRN))
            else:
                return redirect("http://localhost:8000/home/?SRN={}".format(em))
        else:
            error_message = "Invalid username or password."

    return render(request, 'login_page.html', {'error_message': error_message})


