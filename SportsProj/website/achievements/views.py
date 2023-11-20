from django.shortcuts import render
import mysql.connector as sql

def achieveaction(request):
    srn = request.GET.get('SRN')
    m = sql.connect(host="localhost", user="root", passwd="kshitij2803", database="sports")
    cursor = m.cursor()
    print(srn)
    #c = "SELECT s.name, a.position, a.awardorg, a.cashprize FROM student s JOIN achievements a ON s.SRN = a.SRN WHERE s.SRN = '{}' ORDER BY a.cashprize DESC;".format(srn)
    cursor.callproc( 'GetStudentAchievements', [srn,])
    #cursor.execute()
    t=[]
    for i in cursor.stored_results():
        t.append(i.fetchall())

    print(t)
    student_name = ''
    achievements = []

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
    cur = m.cursor()
    d = "SELECT CalculateTotalCashPrize('{}')".format(srn)
    cur.execute(d)
    
    k = tuple(cursor.fetchone())
    print(k)
    
 
    return render(request, 'achievements.html', {'SRN':srn,'Student_name':student_name,'achievements':achievements, 'total':k[0]})
