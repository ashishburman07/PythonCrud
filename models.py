from django.db import models

class Employee(models.Model):
	eid= models.IntegerField()
	ename=models.CharField(max_length= 100)
	designation=models.CharField(max_length= 100)
	contact=models.IntegerField()

