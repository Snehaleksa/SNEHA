from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import auth
from .models import Students,Teacher,Complaints
# Create your views here.






def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(studenthome)
        else:
            context={
                'message':"Invalid credentials"
            }
            return render(request,'login.html',context)
    else:
        return render(request,'login.html')    




def registration(request):
    if request.method=='POST':
        name=request.POST['name']
        username=request.POST['username']
        password=request.POST['password']
        rollno=request.POST['rollno']
        branch=request.POST['branch']
        image=request.FILES['image']
        
        data=Students.objects.create_user(first_name=name,username=username,password=password,RollNo=rollno,Branch=branch,Image=image)
        data.save()
        return HttpResponse("success")
    else:
        return render(request,'reg.html')
    
   


    
def studenthome(request):
    data=Students.objects.get(id=request.user.id)
    return render(request,'studenthome.html',{'data':data}) 
   
    

def edit(request,id):
    data=Students.objects.get(id=id)
    if request.method=='POST':
        data.first_name=request.POST['name']
        data.username=request.POST['username']
        data.password=request.POST['password']
        data.email=request.POST['email']
        
        data.RollNo=request.POST['rollno']
        data.Branch=request.POST['branch']
        if 'Image' in request.FILES:
           data.Image=request.POST['image']
        data.save()
        return redirect(studenthome)
    else:
        return render(request,'edit.html',{'data':data})   

        


def register2(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']        
        data=Teacher.objects.create(username=username,password=password)
        data.save()
        return HttpResponse("success")
    else:
        return render(request,'teacherregister.html') 

def teacherlogin(request):
    if request.method == 'POST':
      username = request.POST.get('username')
      password=request.POST.get('password')
      if Teacher.objects.filter(username=username,password=password).exists():
         userdetail=Teacher.objects.get(username=request.POST['username'],password=password)
         if userdetail.password==request.POST['password']:
            request.session['uid']=userdetail.id 
            return redirect(teacherhome)
         else:
            return render (request,'login2.html')
      else:
         return render(request,'login2.html',{'message':'Invalid Username or password'})
    else:
      return render(request,'login2.html') 



   


def teacherhome(request):  
    tem=request.session['uid']
    data=Teacher.objects.get(id= tem)
    return render(request,'teacherhome.html',{'data':data})

def complaints(request):
    data=Students.objects.get(id=request.user.id)
    
    if request.method=="POST":
        complaint_name=request.POST['Teacher']
        description=request.POST['complaint']
        data1=Complaints.objects.create(user_id=data,complaint_name=complaint_name,description=description)
        data1.save()
        return redirect(studenthome)
    else:
        return render(request,'complaints.html')
    
def viewcomplaints(request):
    data=Students.objects.get(id=request.user.id)
    data1=Complaints.objects.filter(user_id=data)
    return render (request,'viewcomplaints.html',{'data1':data1})


def teacherview(request):
    data1=Students.objects.get(id=request.user.id)
    data=Complaints.objects.filter(user_id=data1)
    return render(request,'teacherview.html',{'data':data})



def reply(request):
    data=Students.objects.get(id=request.user.id)
    if request.method=='POST':
        reply=request.POST['reply']
        data1=Complaints.objects.create(user_id=data,reply=reply)
        data1.save()
        return redirect(teacherview)
    else:
        return render(request,'reply.html')      

def viewreply(request):
    data=Students.objects.get(id=request.user.id)
    data1=Complaints.objects.filter(user_id=data)
    return render (request,'viewcomplaints.html',{'data1':data1})



