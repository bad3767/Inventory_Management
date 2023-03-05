from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home.html"),
    path("add/",views.addshop,name="add.html"),
    path("view/",views.view,name="view.html"),
    path("update/<int:id>",views.update,name="edit.html"),
    path("location_add/",views.location_add,name="location_add.html"),
    path("location_view/",views.location_view,name="location_view.html"),
    path("display1/",views.display_all,name="display.html"),
     
]