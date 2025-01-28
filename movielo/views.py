from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Destination
from .forms import DestinationForm
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DestinationSerializer
from . import models
def homepage(request):
    return render(request, 'homepage.html')
# Create your views here.

def homepage2(request):
     
     dest = models.Destination()
     dest.id= 1
     dest.name= 'HYD'
     dest.desc = 'The old city'
     dest.image = 'destination_1.jpg'
     dest.price = 300

     return render(request,'index.html', {'dest1':dest})

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        uname = request.POST['username']
        pword = request.POST['password']
        if uname=='SVS' and pword == "SVS":
            return render(request, 'homepage.html', {'username':uname})
        else:
            return HttpResponse("<h1>Invalid User Credentials</h1>")


def view_profile(request):
    return HttpResponse("<h1>IN profile view page</h1>")

def edit_profile(request):
    pass

def delete_profile(request):
    pass

def dest_details(request,dest_id):
    dest=list(Destination.objects.filter(id=dest_id))
    if dest:
        return render(request,'destination.html',{'dest':dest[0]})
    


def dest_add(request):
    if request.method=='POST':
        form = DestinationForm(request.POST,request.FILES)
        print(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/hp2/add')
        else:
            messages.info(request,'Error while creating Destination')
    return render(request,'destinationForm.html',{'form':DestinationForm()})


@api_view(['GET'])
def get_all_destinations(request):
    dests=Destination.objects.all()
    serializer=DestinationSerializer(dests,many=True)
    return Response(serializer.data)

