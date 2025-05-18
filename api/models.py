from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meal(models.Model):
    title=models.CharField(max_length=200)
    MEAL_TYPE_OPTIONS=(
        ('breakfast','breakfast'),
        ('brunch','brunch'),
        ('lunch','lunch'),
        ('snack','snack'),
        ('dinner','dinner')
    )
    meal_type=models.CharField(max_length=200,choices=MEAL_TYPE_OPTIONS,default='breakfast')
    calorie=models.IntegerField()
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='meals')
    created_at=models.DateTimeField(auto_now_add=True)