from django.db import models

# Create your models here.
class Guest(models.Model):
    name=models.CharField(max_length=64,unique=False)
    email=models.EmailField(max_length=100,unique=False)
    # CONTACT			: 8000770008
    check_in=models.DateField(unique=False)
    check_out=models.DateField(unique=False,validators=[])
    staff_behaviour=models.IntegerField(choices=[(1,1),(2,2),(3,3),(4,4),(5,5)])
    cleanliness=models.IntegerField(choices=[(1,1),(2,2),(3,3),(4,4),(5,5)])
    food_quality=models.IntegerField(choices=[(1,1),(2,2),(3,3),(4,4),(5,5)])
    overall=models.IntegerField(choices=[(1,1),(2,2),(3,3),(4,4),(5,5)])
    feedback=models.TextField(max_length=1000,unique=False)
