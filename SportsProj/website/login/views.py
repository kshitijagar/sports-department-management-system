
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

        d = "SELECT * FROM student WHERE (emailid='{}' OR SRN='{}') AND password='{}'".format(em, em, pwd)
        cursor.execute(d)
        
        k = tuple(cursor.fetchall())
        
        if k != ():
            
            u="SELECT SRN FROM student WHERE emailid='{}' OR SRN='{}'".format(em, em)
            cursor.execute(u)
            SRN= str(cursor.fetchall()[0])
            SRN=SRN[2:-3]
            print(SRN)
            return redirect("http://localhost:8000/home/?SRN={}".format(SRN))
            
        else:
            error_message = "Invalid username or password."

    return render(request, 'login_page.html', {'error_message': error_message})


