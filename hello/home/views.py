#from django.http import HttpResponse
from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request,'index1.html')
def about(request):
    return render(request,'about.html')
def service(request):
    return render(request,'services.html')
def contact(request):
    if request.method=="POST":
        name = request.POST.get('name' )
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact= Contact(name= name , email= email, phone= phone, desc= desc, date= timezone.now())
        contact.save()
    return render(request,'contact.html')



