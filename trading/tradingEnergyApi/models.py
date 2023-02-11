from django.db import models


class tradeModel (models.Model):

    id= models.CharField(primary_key=True,max_length=100)
    quantity= models.IntegerField(max_length=30)
    price= models.FloatField(max_length=30)
    side= models.CharField(max_length=5, )
    strategy_id= models.CharField(max_length=100)


