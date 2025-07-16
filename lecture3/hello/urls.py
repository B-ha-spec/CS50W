from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("<str:name>", views.greet,name="greet"),
    path("baha",views.baha, name= "baha"),
    path("varvara",views.varvara ,name="varvara")
]
