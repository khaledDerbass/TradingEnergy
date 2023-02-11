#from django.db.backends.sqlite3 import  models.
from django.db import models

class tradeModel (models.Model):
    id= models.CharField(primary_key=True,max_length=100)
    quantity= models.IntegerField
    price= models.FloatField
    side= models.CharField(max_length=5)
    strategy_id= models.CharField(max_length=100)


