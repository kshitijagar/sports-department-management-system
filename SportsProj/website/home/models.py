from django.db import models

class Student(models.Model):
    SRN = models.CharField(max_length=13, primary_key=True)
    name = models.CharField(max_length=30)
    contactno = models.CharField(max_length=10, null=True, blank=True)
    emailid = models.EmailField(max_length=30, null=True, blank=True)
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('B+', 'B+'),
        ('AB+', 'AB+'),
        ('O+', 'O+'),
        ('A-', 'A-'),
        ('B-', 'B-'),
        ('AB-', 'AB-'),
        ('O-', 'O-'),
    ]
    bloodgroup = models.CharField(
        max_length=3,
        choices=BLOOD_GROUP_CHOICES,
        null=True,
        blank=True
    )
    password = models.CharField(max_length=255)
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES
    )

    def __str__(self):
        return self.SRN
    
    class Meta:
        db_table = 'student'
