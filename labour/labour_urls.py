from django.conf.urls import url
from labour import views

urlpatterns = [
    url(r'^v_labours/', views.admin_view_labours, name='admin_view_labours'),
    url(r'^l_home/', views.labour_home, name='labour_home'),
    url(r'^reg/', views.labour_registration, name='labour_registration'),

]