from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("about/",views.about,name="about"),
    path("interests/",views.interests,name="interests"),
    path("location/", views.location, name="location"),
    path("certificate/", views.certificate ,name="certificate"),
    path("contact/", views.contact, name="contact"),
    path("resume/",views.resume,name="resume")
]
