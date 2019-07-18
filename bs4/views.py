from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "bs4/index.html")

def aboutus(request):
    return render(request, "bs4/aboutus.html")

def contactus(request):
    return render(request, "bs4/contactus.html")
