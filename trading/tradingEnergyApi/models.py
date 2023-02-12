from django.db import models

class tradeModel (models.Model):

    id= models.CharField(primary_key=True,max_length=100)
    quantity= models.IntegerField(max_length=30)
    price= models.FloatField(max_length=30)

    # In Django null=False & blank=False is default, so there's no need to specify nullable check in the model
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#null
    side_choices =(
         ("BUY", "buy"),
    ("SELL", "sell"),
    ) 
    side= models.CharField(max_length=5,choices=side_choices,default='N/A')
    strategy= models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'epex_12_20_12_13'


