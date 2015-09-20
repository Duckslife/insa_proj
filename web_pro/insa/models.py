from django.db import models

# Create your models here.
class Employee(models.Model) :
     id = models.IntegerField( db_column='id', primary_key=True)
     name = models.CharField(max_length=255, db_column='name')
     role= models.CharField(max_length=255, db_column='role')
     division = models.CharField(max_length=255, db_column='division')



class Grade(models.Model):
    id = models.IntegerField( db_column='id', primary_key=True)
    course_name = models.CharField(max_length=255, db_column='course_name')
    subject_name= models.CharField(max_length=255, db_column='subject_name')
    grade = models.IntegerField(db_column='grade')
    standard = models.IntegerField(db_column='standard')
