from django.shortcuts import render, redirect
import mysql.connector as sql

# Global variables to store form data temporarily
fn = ''
ln = ''
s = ''
em = ''
pwd = ''

# View for handling user sign-up
def signaction(request):
    # Access global variables
    global fn, ln, s, em, pwd

    # Check if the request method is POST
    if request.method == "POST":
        # Connect to the MySQL database
        m = sql.connect(host="localhost", user="root", passwd="kshitij2803", database="sports")
        cursor = m.cursor()

        # Extract form data and store in global variables
        d = request.POST
        for key, value in d.items():
            if key == "name":
                n = value
            if key == "SRN":
                SRN = value
            if key == "sex":
                s = value
            if key == "email":
                em = value
            if key == "password":
                pwd = value
            if key == "mobile":
                mob = value
            if key == "bg":
                bg = value

        # Create SQL query to insert user data into the 'student' table
        c = "INSERT INTO student VALUES('{}','{}','{}','{}','{}', '{}', '{}')".format(SRN, n, mob, em, bg, pwd, s)
        cursor.execute(c)

        # Commit changes to the database
        m.commit()

        # Redirect to the login page after successful sign-up
        return redirect('http://localhost:8000/login/')

    # Render the 'signup_page.html' template if the request method is not POST
    return render(request, 'signup_page.html')
