# Generated by Django 3.1.7 on 2023-03-05 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='display1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product', models.CharField(max_length=50)),
                ('Product_ID', models.IntegerField()),
                ('Product_Quantity', models.IntegerField()),
                ('Product_Location', models.CharField(max_length=50)),
                ('Product_Loc_Id', models.IntegerField()),
                ('Product_warehouse', models.DecimalField(blank=True, decimal_places=0, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location_Name', models.CharField(max_length=50)),
                ('Location_ID', models.IntegerField()),
                ('Warehouse_No', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='shops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_Name', models.CharField(max_length=50)),
                ('Product_Name', models.CharField(max_length=50)),
                ('Location_Name', models.CharField(max_length=50)),
                ('Product_ID', models.IntegerField()),
                ('Quantity', models.IntegerField()),
            ],
        ),
    ]
