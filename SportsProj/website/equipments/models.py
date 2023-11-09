from django.db import models

class Equipment(models.Model):
    equipid = models.CharField(max_length=10, primary_key=True)
    equipname = models.CharField(max_length=15)
    buydate = models.DateField(null=True, blank=True)
    availability = models.IntegerField(default=1)

    def __str__(self):
        return self.equipid
    
    class Meta:
        db_table = 'equipment'
