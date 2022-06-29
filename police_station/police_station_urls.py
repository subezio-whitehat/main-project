from django.conf.urls import url
from police_station import views


urlpatterns = [
    url(r'^verify_labours/', views.verify_labours, name='verify_labours'),
    url(r'^reg/', views.admin_reg_police, name='admin_reg_police'),
    url(r'^manage/', views.admin_manage_police, name='admin_manage_police'),
    url(r'^p_home/', views.police_home, name='police_home'),
    url(r'^a_update_p/(?P<pid>\w+)', views.admin_update_police, name='admin_update_police'),
    url(r'^approve/(?P<lid>\w+)', views.police_approve_labours, name='police_approve_labours'),

]