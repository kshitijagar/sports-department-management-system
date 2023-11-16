from django.db import models
from home.models import Student
from .models import Court

class Booking(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField(null=True, blank=True)
    SRN = models.ForeignKey(Student, on_delete=models.CASCADE,db_column='SRN')
    courtid = models.ForeignKey(Court, on_delete=models.CASCADE,db_column='courtid',primary_key=True)

    def __str__(self):
        return f'Booking for {self.SRN} at {self.courtid} ({self.start_time}-{self.end_time})'

    class Meta:
        db_table = 'bookings'
