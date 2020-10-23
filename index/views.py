
from django.shortcuts import render,HttpResponse
from datetime import date
from .models import Contact,Blog,Tutorial
from django.contrib import messages

# Create your views here.
from django.http import HttpResponse
import datetime



def index(request):
    return  render(request,"index.html")
def about(request):
    return  render(request,"about.html")
def blog(request):
    blogs=Blog.objects.all().order_by("-date")
    return  render(request,"blog.html",{'blogs':blogs})

def tutorials_cs3(request):
    head="Photoshop Cs3 Tutorials"

    tutorials=Tutorial.objects.all().filter(type ='CS3')

    return  render(request,"tutorials.html",{"tutorials":tutorials,"head":head})
def tutorials_cc(request):
    head = "Photoshop CC Tutorials"
    tutorials = Tutorial.objects.all().filter(type='CC')

    return render(request, "tutorials.html", {"tutorials": tutorials, "head": head})
def tutorials(request):
    head = "Photoshop Tutorials"
    tutorials = Tutorial.objects.all()

    return render(request, "tutorials.html", {"tutorials": tutorials, "head": head})
# def search(request):
#     keyword=request.GET['keywords']
#     blogs = Tutorial.objects.filter(name__icontains=keyword)
#     return render(request, "blog.html", {'blogs': blogs})

def search(request):
    keyword=request.GET['query']
    blogs = Blog.objects.filter(title__icontains=keyword)

    return render(request, "search.html", {'blogs': blogs})
def contact(request):
    if request.method=='POST':
        f_name=request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        msg = request.POST.get('msg')


        contact=Contact(f_name=f_name,l_name=l_name,email=email,phone=phone,msg=msg,date=date.today())
        contact.save()
        messages.success(request,"Your Message Has Been Sent!")

    return  render(request,"contact.html")