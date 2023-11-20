from django.shortcuts import render
import mysql.connector as sql

def achieveaction(request):
    # Get SRN parameter from the request's GET parameters
    srn = request.GET.get('SRN')

    # Connect to the MySQL database
    m = sql.connect(host="localhost", user="root", passwd="kshitij2803", database="sports")
    cursor = m.cursor()

    # Call the stored procedure 'GetStudentAchievements' with the provided SRN
    cursor.callproc('GetStudentAchievements', [srn,])
    t = []

    # Fetch results from the stored procedure and store in list 't'
    for i in cursor.stored_results():
        t.append(i.fetchall())

    # Print the fetched results
    print(t)

    # Initialize variables for student name and achievements
    student_name = ''
    achievements = []

    # Extract information from the fetched results and store in 'achievements' list
    for j in t:
        for i in j:
            a = str(i)
            a = a[1:-1]
            s = a.split(", ")
            student_name = s[0][1:-1]
            achievements.append({
                'position': s[1],
                'awardorg': s[2][1:-1],
                'cashprize': s[3]
            })

    # Create a new cursor for a separate query
    cur = m.cursor()

    # Execute a query to calculate the total cash prize for the given SRN
    d = "SELECT CalculateTotalCashPrize('{}')".format(srn)
    cur.execute(d)

    # Fetch the result of the query and store in variable 'k'
    k = tuple(cursor.fetchone())
    print(k)

    # Render the 'achievements.html' template with the obtained data
    return render(request, 'achievements.html', {'SRN': srn, 'Student_name': student_name, 'achievements': achievements, 'total': k[0]})
