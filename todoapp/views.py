from django.shortcuts import render,redirect
from .models import List ,ListForm
def add_list(request):
    if request.method=="POST":
        f=ListForm(request.POST)
        f.save()
        return redirect('/')
    else:
        context={'form':ListForm}
        return render(request,"addlist.html",context)


def todo_show(request):
    uid=request.session.get("uid")
    show=List.objects.filter(user=uid)
    context={'sho':show}
    return render(request,"todoshow.html",context)

def delete_list(request,id):
    show=List.objects.get(id=id)
    show.delete()
    return redirect('/')

def edit_list(request,id):
    show=List.objects.get(id=id)
    if request.method=="POST":
        f=ListForm(request.POST,instance=show)
        f.save()
        return redirect('/')
    
    else:
        show=ListForm(instance=show)
        context={'form':show}
        return render(request,"editlist.html",context)
