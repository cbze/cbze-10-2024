from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=255)
    currently_in = models.CharField(max_length=100)
    school = models.CharField(max_length=250)
    mobile_no = models.CharField(max_length=12)
    roll_no = models.CharField(max_length=12)
    
    #result
    hindi = models.IntegerField()
    english = models.IntegerField()
    science = models.IntegerField()
    social_science = models.IntegerField()
    maths = models.IntegerField()
    computer = models.IntegerField()

    status = models.CharField(max_length=100)
    color = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return str(self.name)