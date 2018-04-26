from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Planner(models.Model):
	sub1 = models.CharField(max_length = 100, blank = True)
	subhours1 = models.FloatField(blank = True)
	sub2 = models.CharField(max_length = 100, blank = True)
	subhours2 = models.FloatField(blank = True)
	sub3 = models.CharField(max_length = 100, blank = True)
	subhours3 = models.FloatField(blank = True)
	sub4 = models.CharField(max_length = 100, blank = True)
	subhours4 = models.FloatField(blank = True)
	sub5 = models.CharField(max_length = 100, blank = True)
	subhours5 = models.FloatField(blank = True)
	sub6 = models.CharField(max_length = 100, blank = True)
	subhours6 = models.FloatField(blank = True)
	student = models.ForeignKey(User, on_delete=models.CASCADE)

