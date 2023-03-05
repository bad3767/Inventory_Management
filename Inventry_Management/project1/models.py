from django.db import models

# Create your models here.
class shops(models.Model):
    Customer_Name=models.CharField(max_length=50)
    Product_Name=models.CharField(max_length=50)
    Location_Name=models.CharField(max_length=50)
    Product_ID=models.IntegerField()
    Quantity=models.IntegerField()
    

class location(models.Model):
    Location_Name=models.CharField(max_length=50)
    Location_ID=models.IntegerField()
    Warehouse_No=models.IntegerField()


                            
class display1(models.Model):
    Product=models.CharField(max_length=50)
    Product_ID=models.IntegerField()
    Product_Quantity=models.IntegerField()
    Product_Location=models.CharField(max_length=50)
    Product_Loc_Id=models.IntegerField()
    Product_warehouse=models.DecimalField(max_digits=5,decimal_places=0 ,blank=True,null=True)