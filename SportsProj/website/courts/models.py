# models.py in your app (e.g., courts)
from django.db import models

class Court(models.Model):
    courtid = models.CharField(max_length=5, primary_key=True)
    courttype = models.CharField(max_length=15,null=True,default=None)
    courtdesc = models.CharField(max_length=30,null=True,default=None)
    avail = models.IntegerField(default=1)
    def __str__(self):
        return self.courtid

    class Meta:
        db_table = 'court'