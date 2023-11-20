from django.shortcuts import render, redirect
import mysql.connector as sql

# Global variables to store form data temporarily
cp = ''
tit = ''
dat = ''
pos = ''
SRN = ''

# View for adding achievements
def addachaction(request):
    # Access global variables
    global cp, tit, SRN, pos, dat

    # Get SRN parameter from the request's GET parameters
    SRN = request.GET.get('SRN')

    # Check if the request method is POST
    if request.method == "POST":

        # Connect to the MySQL database
        m = sql.connect(host="localhost", user="root", passwd="kshitij2803", database="sports")
        cursor = m.cursor()

        # Extract form data and store in global variables
        d = request.POST
        for key, value in d.items():
            if key == "cp":
                cp = value
            if key == "titl":
                tit = value
            if key == "aDate":
                dat = value
            if key == "pos":
                pos = value
        # Create SQL query to insert data into the 'achievements' table
        c = "INSERT INTO achievements(recorddate, position, awardorg, cashprize, SRN) VALUES('{}','{}','{}','{}','{}')".format(dat, pos, tit, cp, SRN)
        # Execute the query
        cursor.execute(c)
        # Commit changes to the database
        m.commit()
        # Redirect to the achievements page for the given SRN
        return redirect('http://localhost:8000/achievement/?SRN={}'.format(SRN))
    # Render the 'add_achievement.html' template with the SRN parameter
    return render(request, 'add_achievement.html', {'SRN': SRN})
