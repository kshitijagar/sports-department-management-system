from django.shortcuts import render, redirect
import mysql.connector as sql

# Global variables to store email and password temporarily
em = ''
pwd = ''

# View for handling login
def loginaction(request):
    # Access global variables
    global em, pwd

    # Initialize error_message
    error_message = ''

    # Check if the request method is POST
    if request.method == "POST":
        # Connect to the MySQL database
        m = sql.connect(host="localhost", user="root", passwd="kshitij2803", database="sports")
        cursor = m.cursor()

        # Extract email and password from the form data
        d = request.POST
        for key, value in d.items():
            if key == "email":
                em = value
            if key == "password":
                pwd = value

        # Create SQL query to check if the provided credentials are valid
        d = "SELECT * FROM student WHERE (emailid='{}' OR SRN='{}') AND password='{}'".format(em, em, pwd)
        cursor.execute(d)

        # Fetch results from the query
        k = tuple(cursor.fetchall())

        # Check if a user with the provided credentials exists
        if k != ():
            # Retrieve the SRN of the user for redirection
            u = "SELECT SRN FROM student WHERE emailid='{}' OR SRN='{}'".format(em, em)
            cursor.execute(u)
            SRN = str(cursor.fetchall()[0])
            SRN = SRN[2:-3]

            # Debugging statement
            print(SRN)

            # Redirect to the home page with the SRN parameter
            return redirect("http://localhost:8000/home/?SRN={}".format(SRN))

        else:
            # Set error_message if credentials are invalid
            error_message = "Invalid username or password."

    # Render the 'login_page.html' template with the error message
    return render(request, 'login_page.html', {'error_message': error_message})
