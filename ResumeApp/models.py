from django.db import models

# Create your models here.

class Resume(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Dob = models.DateField()
    Number = models.IntegerField()
    Gender = models.CharField(max_length=20)
    Birth_place = models.CharField(max_length=50)
    Summary = models.TextField()
    Ssc_year = models.CharField(max_length=30)
    Ssc_school = models.CharField(max_length=50)
    Ssc_board = models.CharField(max_length=50)
    Ssc_aggregate = models.FloatField()
    Hsc_year = models.CharField(max_length=30)
    Hsc_school = models.CharField(max_length=50)
    Hsc_board = models.CharField(max_length=50)
    Hsc_aggregate = models.FloatField()
    Ug_year = models.CharField(max_length=30)
    Ug_collage = models.CharField(max_length=50)
    Ug_board = models.CharField(max_length=50)
    Ug_aggregate = models.FloatField()
    Technical_skill = models.CharField(max_length=100)
    Project = models.TextField()
    Internship = models.CharField(max_length=100)
    Certificate = models.CharField(max_length=150)
    Language_known = models.CharField(max_length=100)
    Hobbies = models.CharField(max_length=100)

