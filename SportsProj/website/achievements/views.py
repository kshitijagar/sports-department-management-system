from django.shortcuts import render
import mysql.connector as sql

def achieveaction(request):
    srn = request.GET.get('SRN')
    m = sql.connect(host="localhost", user="root", passwd="JugguSQL@123", database="sports")
    cursor = m.cursor()
    c = "SELECT s.name, a.position, a.awardorg, a.cashprize FROM student s JOIN achievements a ON s.SRN = a.SRN WHERE s.SRN = '{}' ORDER BY a.cashprize DESC;".format(srn)
    cursor.execute(c)
    t = list(cursor.fetchall())
    student_name = ''
    achievements = []

    for i in t:
        a = str(i)
        a = a[1:-1]
        s = a.split(", ")
        student_name = s[0]
        achievements.append({
            'position': s[1],
            'awardorg': s[2],
            'cashprize': s[3]
        })

    context = {
        'SRN': srn,
        'Student_name': student_name,
        'achievements': achievements
    }
    print(context)
    return render(request, 'achievements.html', context)
