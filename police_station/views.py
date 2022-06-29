from django.shortcuts import render
from login.models import Login
from labour.models import Labour
from police_station.models import PoliceStation

def verify_labours(request):
    po_lg=request.session["pid"]        #police's login id
    po_id=Login.objects.get(login_id=po_lg)     #police id
    police=PoliceStation.objects.get(p_id=po_id.user_id)     #police district
    lab=Labour.objects.filter(district=police.district,status="pending")
    context={
        'laa':lab,
    }
    return render(request,'police_station/p_verify_labours.html',context)


def admin_reg_police(request):
    if request.method == "POST":
        ph = request.POST.get("phone")
        if PoliceStation.objects.filter(phone=ph).exists():
            inn = "Already registred using this number!!!"
            context = {
                'inn': inn,
            }
            return render(request, 'police_station/registration.html', context)
        else:
            ob=PoliceStation()
            ob.station_name=request.POST.get("station_name")
            ob.addresss=request.POST.get("address")
            ob.phone=request.POST.get("phone")
            ob.email=request.POST.get("email")
            ob.district=request.POST.get("district")
            ob.username=request.POST.get("username")
            ob.password=request.POST.get("password")
            ob.save()

            obj=Login()
            obj.username=request.POST.get("username")
            obj.password=request.POST.get("password")
            obj.type="police station"
            obj.user_id=ob.p_id
            obj.save()
    return render(request,'police_station/registration.html')


def admin_manage_police(request):
    ob=PoliceStation.objects.all()
    context={
        'po':ob,
    }
    return render(request,'police_station/a_manage_p.html',context)

def police_home(request):
    return render(request,'police_station/p_home.html')

def admin_update_police(request,pid):
    ob=PoliceStation.objects.filter(p_id=pid)
    context={
        'pp':ob,
    }
    if request.method=="POST" and 'update' in request.POST:
        obj=PoliceStation.objects.get(p_id=pid)
        obj.p_id=request.POST.get("id")
        obj.station_name=request.POST.get("station_name")
        obj.addresss=request.POST.get("address")
        obj.phone=request.POST.get("phone")
        obj.email=request.POST.get("email")
        obj.district=request.POST.get("district")
        obj.save()
        return admin_manage_police(request)

    if request.method=="POST" and 'delete' in request.POST:
        obb=PoliceStation.objects.get(p_id=pid).delete()
        return admin_manage_police(request)

    return render(request,'police_station/a_update_p.html',context)

def police_approve_labours(request,lid):
    ob=Labour.objects.filter(l_id=lid)
    context={
        'paa': ob,
    }
    if request.method=="POST":
        obj=Labour.objects.get(l_id=lid)
        obj.status="labour"
        obj.save()

        lab=Labour.objects.get(l_id=lid)
        obb=Login.objects.get(user_id=lid,username=lab.username,password=lab.password)
        obb.type="labour"
        obb.save()
        return verify_labours(request)
    return render(request,'police_station/p_approve_labours.html',context)