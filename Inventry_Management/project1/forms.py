from django import forms
from.models import shops,location

class shopform(forms.ModelForm):
    class Meta:
        model=shops
        fields=[
            "Customer_Name",
            "Product_Name",
            "Location_Name",
            "Product_ID",
            "Quantity",
        ]

class locationform(forms.ModelForm):
    class Meta:
        model=location
        fields=[
            "Location_Name",
            "Location_ID",
            "Warehouse_No",
        ]