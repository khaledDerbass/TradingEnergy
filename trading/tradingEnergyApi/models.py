#from django.db.backends.sqlite3 import  models.
from django.db import models

class tradeModel (models.Model):
    id= models.CharField 
    price= models.FloatField
    quantity= models.IntegerField
    side= models.CharField
    strategy_id= models.CharField
