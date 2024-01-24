from django.shortcuts import render,HttpResponsePermanentRedirect
from .forms import studentRegistration
from .models import User

# Create your views here.
#add and show data
def add_show(request):
    if request.method=='POST':
        fm=studentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            ps=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=ps)
            reg.save()
            fm=studentRegistration() 
    else:
        fm=studentRegistration() 
    stud=User.objects.all()
    return render(request,'fisrtapp/addandshow.html',{'form':fm,'stu':stud})

#update and edit
def update_data(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        fm=studentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=studentRegistration(instance=pi)
    return render(request,'fisrtapp/updatestudent.html',{'form':fm})

#delete function
def delete_data(request,id):
    if request.method=='POST':
        pi= User.objects.get(pk=id)
        pi.delete()
        return HttpResponsePermanentRedirect('/')


