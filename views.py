from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse
# Create your views here.
def index(request):
    if request.method=="POST":
        name=request.POST.get('name' , ' ')
        sem=request.POST.get('sem' , ' ')
        phone=request.POST.get('phone' , ' ')
        email=request.POST.get('email' , ' ')
        if name and sem and phone and email:
            contact=Contact(name=name,sem=sem,phone=phone,email=email)
            contact.save()
        else:
            return HttpResponse("Enter Full Details")
    return render(request,'index.html')