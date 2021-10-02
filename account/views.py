from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate

def home(request):
    return render(request,'home.html')


def register(request):
    if request.method=='POST':
        f=UserCreationForm(request.POST)
        f.save()
        return redirect("/")
    else:
        context={'form':UserCreationForm}
        return render(request,'adduser.html',context)

def login_view(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        passw=request.POST.get('passw')
        user=authenticate(request,username=uname,password=passw)

        if user is not None:
            request.session['uid']=user.id
            login(request,user)
            return redirect('/')
        else:
            context={'lmsg':"UserName And Passwprd is Not Valid"}
            return render(request,"login.html",context)
    else:
        return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('/')