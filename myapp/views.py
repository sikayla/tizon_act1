# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage


# Create your views here.
def home(request):
    return render (request,"home.html")

def about (request):
    return render (request,"about.html")


def interests (request):
    interests_show=[
        {
            'title': 'Cyber Security',
            'path': 'images/cs.PNG',
        },
        {
           'title': 'Networking',
            'path': 'images/netw.JPG',
        },
        {
            'title': 'Coding',
            'path': 'images/codes.PNG',
        },
        {
            'title': 'Software Development',
            'path': 'images/software1.PNG',
        },
        {
            'title': 'Web Development',
            'path': 'images/web.PNG',
        },
        {
            'title': 'Game Development',
            'path': 'images/game.PNG',
        },
         
    ]
    return render (request,"interests.html",{"interests_show": interests_show})


def location(request):
    location=[
        {"company":"ABC",
         "position":"python developer"},
        {"company":"ABC2",
         "position":"python developer2"},
        {"company":"ABC3",
         "position":"python developer3"}
    ]
    return render (request,"location.html",{"location":location})


def certificate(request):
    return render (request, "certificate.html")


def contact(request):
    return render (request,"contact.html")

def resume(request):
    resume_path="myapp/resume.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response['Content-Disposition']='attachment';filename="resume.pdf"
            return response
    else:
        return HttpResponse("resume not found", status=404)