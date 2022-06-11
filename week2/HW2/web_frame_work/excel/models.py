from django.db import models

# Create your models here.
class Student(models.Model):
    school = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    student_id = models.CharField(max_length=50, unique= True)
    stu_class = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    date = models.CharField(max_length=200)
    sex = models.CharField(max_length=20)
    place_of_birth = models.CharField(max_length=100)
    ethnic = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    phone_number = models.IntegerField(blank=True)
    total_grade_1 = models.PositiveSmallIntegerField(blank=True)
    total_grade_2 = models.PositiveSmallIntegerField(blank=True)
    total_grade_3 = models.PositiveSmallIntegerField(blank=True)
    total_grade_4 = models.PositiveSmallIntegerField(blank=True)
    total_grade_5 = models.PositiveSmallIntegerField(blank=True)
    total_5_years = models.PositiveSmallIntegerField(blank=True)
    plus = models.PositiveSmallIntegerField(blank=True, null= True, default=0)
    total_all = models.PositiveSmallIntegerField(blank=True, null=True)
    decripsion = models.CharField(max_length=255)

    def __str__(self):
        return self.name