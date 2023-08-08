from django.shortcuts import render
from django.http import HttpResponse

def main_menu (request):
    return render(request,"new_app/home.html")
def main_home(request):
    return render(request,"new_app/home.html")
def main_about(request):
    return render(request,"new_app/about.html")
def main_contact(request):
    return render(request,"new_app/contact.html")