from django.db import models
import datetime
# Create your models here.
class Item_sale(models.Model):
    
    item_name = models.CharField(max_length=255)
    item_id = models.IntegerField()
    item_price = models.IntegerField()
    quantity_bought = models.IntegerField()
    date = models.DateField(default=datetime.date.today)

    def __str__(self):

        return self.item_name+" with id : "+str(self.item_id)+" is sold "+str(self.quantity_bought)+" pieces , at "+str(self.date)


class Item_purchase(models.Model):

    item_id = models.IntegerField()
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    purchase_quantity = models.DecimalField(max_digits=5 , decimal_places=3)
    kitchen_issue = models.DecimalField(max_digits=5 , decimal_places=3)
    stock = models.DecimalField(max_digits=5, decimal_places=3)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return "Id : "+str(self.item_id)+" , Name : "+self.name+" , Date : "+str(self.date)+" , Time : "+str(self.time)