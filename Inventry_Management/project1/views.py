from django.shortcuts import render,redirect,get_object_or_404
from .models import shops,location,display1
from. forms import shopform,locationform
from decimal import Decimal
# Create your views here.
def home(request):
    return render(request,'home.html')

def addshop(request):
    obj=shopform (request.POST or None)
    if obj.is_valid():
        obj.save()
        return redirect("/view/")
    return render (request,"add.html",{"hello":obj})

def view(request):
    aa={}
    aa["data"]=shops.objects.all()
    return render (request,"view.html",aa)

def update(request,id):
    dd={}
    obj=get_object_or_404(shops,pk=id)
    ss=shopform(request.POST , instance=obj)
    if ss.is_valid():
        ss.save()
        return redirect('/view/')
    dd['o']=ss
    return render(request,"edit.html",dd)

def location_add(request):
    obj= locationform(request.POST or None)
    if obj.is_valid():
        obj.save()
        return redirect("/location_view/")
    return render(request,"location_add.html",{"ll":obj})

def location_view(request):
    zz={}
    zz["data1"]=location.objects.all()
    return render(request,"location_view.html",zz)

def display_all(request):
    if request.method=="POST":
        l_name=request.POST.get('Location_Name')
        pr=shops.objects.get(id=l_name)
        lc=location.objects.get(id=l_name)
        print("aa")
        if True:
            pn=pr.Product_Name
            pid=pr.Product_ID
            pqt=pr.Quantity
            ln=pr.Location_Name
            lid=lc.Location_ID
            wh=lc.Warehouse_No
            dis=display1.objects.create(Product=pn,
                                       Product_ID=pid,
                                       Product_Quantity=pqt,
                                       Product_Location=ln,
                                       Product_Loc_Id=lid,
                                       Product_warehouse=wh)
            print(dis.id)
            return render(request,"display.html",locals())
    return render(request,"display.html",locals())

