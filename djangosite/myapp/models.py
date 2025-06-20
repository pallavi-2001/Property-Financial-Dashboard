from django.db import models

# Create your models here.
class Data(models.Model):
    name=models.CharField(max_length=200)
    price=models.FloatField()
    rent=models.FloatField()
    emi=models.FloatField()
    tax=models.FloatField()
    expense=models.FloatField()
    expense_monthly=models.FloatField(default=0)
    income_monthly=models.FloatField(default=0)
