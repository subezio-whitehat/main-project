from django.shortcuts import render
from labour.models import Labour
from django.core.files.storage import FileSystemStorage
from login.models import Login

def admin_view_labours(request):
    ob=Labour.objects.all().exclude(status="pending")
    context={
        'lab':ob,
    }
    return render(request,'labour/a_view_labours.html',context)


def labour_home(request):
    return render(request,'labour/home.html')


def labour_registration(request):
    if request.method=="POST":
        ob=Labour()
        ob.name=request.POST.get("name")
        ob.address=request.POST.get("address")
        ob.phone=request.POST.get("phone")
        ob.email=request.POST.get("email")
        ob.skill=request.POST.get("skill")
        ob.district=request.POST.get("district")
        ob.username=request.POST.get("username")
        ob.password=request.POST.get("password")
        ob.status="pending"

        file=request.FILES['photo']
        ff=FileSystemStorage()
        filename=ff.save(file.name,file)
        ob.photo=file.name
        ob.save()

        obj=Login()
        obj.username=request.POST.get("username")
        obj.password=request.POST.get("password")
        obj.type="pending"
        obj.user_id=ob.l_id
        obj.save()
    return render(request,'labour/registration.html')