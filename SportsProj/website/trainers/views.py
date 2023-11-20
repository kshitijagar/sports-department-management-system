from django.shortcuts import render
import mysql.connector as sql

# View for displaying trainer information for a specific student
def trainaction(request):
    # Get SRN parameter from the request's GET parameters
    srn = request.GET.get('SRN')

    # Connect to the MySQL database
    m = sql.connect(host="localhost", user="root", passwd="kshitij2803", database="sports")
    cursor = m.cursor()

    # SQL query to fetch trainer information for the given student
    c = "SELECT t.trainername, t.trainerspec, st.name, s.start_date, s.end_date FROM student_trainer s JOIN trainer t ON s.trainerid = t.trainerid JOIN student st ON s.SRN = st.SRN WHERE s.SRN = '{}';".format(srn)
    cursor.execute(c)

    # Fetch results from the query and store in list 't'
    t = list(cursor.fetchall())

    # Initialize variables for student name and achievements
    student_name = ''
    achievements = []

    # Process each row of the fetched results and store in 'achievements' list
    for i in t:
        a = str(i)
        a = a[1:-1]
        s = a.split("', ")
        ss = s[3].split('), ')
        sd = ss[0][14:]
        ed = ss[1][14:-1]
        student_name = s[2][1:]
        achievements.append({
            'tname': s[0][1:],
            'Specialization': s[1][1:],
            's_date': sd,
            'e_date': ed
        })

    # Create context dictionary for rendering the template
    context = {
        'SRN': srn,
        'Student_name': student_name,
        'achievements': achievements
    }

    # Debugging statement
    print(context)

    # Render the 'trainer.html' template with the context data
    return render(request, 'trainer.html', context)
