from django.shortcuts import render

# Create your views here.
from .models import validate
from django.http import HttpResponse
# Create your views here.
def insert(request):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        gender=request.POST['gender']
        mail=request.POST['mail']
        qualification=request.POST['qualification']
        percentage=request.POST['percentage']
        place=request.POST['place']
        phone=request.POST['phone']
        k=validate(name=name,age=age,gender=gender,mail=mail,qualification=qualification,percentage=percentage,place=place,phone=phone)
        k.save()
        return HttpResponse("Record Inserted")
    return render(request,"form.html")


def home(request):
    if request.method=="GET":
        k=validate.objects.all()
        return render(request,"rt.html",{'k':k})