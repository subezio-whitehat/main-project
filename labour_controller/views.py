from django.shortcuts import render
from labour_controller.models import LabourController
from login.models import Login
from labour.models import Labour
from work.models import Work
from user.models import User


def assign_work(request,wid):
    la_lg=request.session["lcid"]      #lc's login id
    la_id=Login.objects.get(login_id=la_lg)   #lc's id
    lc=LabourController.objects.get(lc_id=la_id.user_id)    #lc district
    labs=Labour.objects.filter(district=lc.district).exclude(status="pending")    #approved labours in same district
    context={
        'labb':labs,
    }
    if request.method=="POST":
        lab=request.POST.get("labour")
        ob=Work.objects.get(w_id=wid)
        ob.labour_id=lab
        ob.status="accepted"
        ob.save()
        return view_w_from_user(request)
    return render(request,'labour_controller/assign_work.html',context)


def labour_controller_reg(request):
    if request.method=="POST":
        ph=request.POST.get("phone")
        if LabourController.objects.filter(phone=ph).exists():
            inn = "Already registred using this number!!!"
            context = {
                'inn': inn,
            }
            return render(request, 'labour_controller/registration.html', context)
        else:
            ob=LabourController()
            ob.name=request.POST.get("name")
            ob.address=request.POST.get("address")
            ob.phone=request.POST.get("phone")
            ob.email=request.POST.get("email")
            ob.district=request.POST.get("district")
            ob.username=request.POST.get("username")
            ob.password=request.POST.get("password")
            ob.save()

            obj=Login()
            obj.username=request.POST.get("username")
            obj.password=request.POST.get("password")
            obj.type="labour controller"
            obj.user_id=ob.lc_id
            obj.save()
    return render(request,'labour_controller/registration.html')


def view_w_from_user(request):
    lc_lg=request.session["lcid"]   #lc's login id
    lc_id=Login.objects.get(login_id=lc_lg)     #lc's id
    lc=LabourController.objects.get(lc_id=lc_id.user_id)    #lc's district
    user=User.objects.filter(district=lc.district).values_list('u_id')   #users in same district
    work=Work.objects.filter(user_id__in=user,status="pending")
    context={
        'wk':work,
    }
    return render(request,'labour_controller/view_w_from_u.html',context)


def view_w_status(request):
    la_lg = request.session["lcid"]  # lc's login id
    la_id = Login.objects.get(login_id=la_lg)  # lc's id
    lc = LabourController.objects.get(lc_id=la_id.user_id)  # lc district
    labs = Labour.objects.filter(district=lc.district)  # labours in same district
    work=Work.objects.filter(labour_id__in=labs)
    context={
        'sta':work ,
    }
    return render(request,'labour_controller/view_work_status.html',context)


def labour_controller_home(request):
    return render(request,'labour_controller/home.html')

