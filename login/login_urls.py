from django.conf.urls import url
from login import views


urlpatterns = [
    url(r'^home/', views.main_home, name='main_home'),
    url(r'^a_home/', views.admin_home, name='admin_home'),

]