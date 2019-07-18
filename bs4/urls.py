from . import views
from django.urls import path
urlpatterns = [
    path("",views.index,name="index"),
    path("aboutus/",views.aboutus,name="aboutus"),
    path("contactus/",views.contactus,name="contactus"),
]