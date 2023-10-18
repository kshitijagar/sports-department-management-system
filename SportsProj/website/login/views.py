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

        c = "select * from users where email='{}' and password='{}'".format(em, pwd)
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        if t != ():
            return render(request, "welcome.html")
        else:
            error_message = "Invalid username or password."

    return render(request, 'login_page.html', {'error_message': error_message})
