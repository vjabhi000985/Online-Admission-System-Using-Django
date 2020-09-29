from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'dashboard.html')

def contact(request):
    return render(request,'templates/contact.html')



# Create your views here.
