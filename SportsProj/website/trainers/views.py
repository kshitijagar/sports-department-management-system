from django.shortcuts import render
import mysql.connector as sql

def trainaction(request):
    srn = request.GET.get('SRN')
    m = sql.connect(host="localhost", user="root", passwd="JugguSQL@123", database="sports")
    cursor = m.cursor()
    c = "SELECT t.trainername, t.trainerspec, s.start_date, s.end_date FROM student_trainer s JOIN trainer t ON s.trainerid = t.trainerid WHERE s.SRN = '{}' ;".format(srn)
    cursor.execute(c)
    t = list(cursor.fetchall())
    student_name = ''
    achievements = []
    q="SELECT name from student where SRN='{}'".format(srn)
    cursor=m.cursor()
    cursor.execute(q)
    y=list(cursor.fetchall())
    student_name=str(y)[3:-4]
    print(t)
    for i in t:
        a = str(i)
        a = a[1:-1]
        s = a.split("', ")
        ss=s[2].split('), ')
        sd=ss[0][14:]
        ed= ss[1][14:-1]
        achievements.append({
            'tname': s[0][1:],
            'Specialization': s[1][1:],
            's_date':sd,
            'e_date': ed
        })
    
    context = {
        'SRN': srn,
        'Student_name': student_name,
        'achievements': achievements
    }
    print(context)
    return render(request, 'trainer.html', context)
