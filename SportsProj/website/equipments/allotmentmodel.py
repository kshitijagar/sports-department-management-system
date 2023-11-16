from django.db import models
from home.models import Student
from .models import Equipment

class Allotment(models.Model):
    allot_time = models.TimeField()
    returntime = models.TimeField()
    SRN = models.ForeignKey(Student, on_delete=models.CASCADE,db_column='SRN')
    equipid = models.ForeignKey(Equipment, on_delete=models.CASCADE,db_column='equipid',primary_key=True)

    def __str__(self):
        return f'Allotment for {self.SRN} - {self.equipid}'

    class Meta:
        db_table = 'allotments'