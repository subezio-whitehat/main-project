from django.conf.urls import url
from labour_controller import views


urlpatterns = [
    url(r'^assign_work/(?P<wid>\w+)', views.assign_work, name='assign_work'),
    url(r'^reg/', views.labour_controller_reg, name='labour_controller_reg'),
    url(r'^v_work/', views.view_w_from_user, name='view_w_from_user'),
    url(r'^v_status/', views.view_w_status, name='view_w_status'),
    url(r'^lc_home/', views.labour_controller_home, name='labour_controller_home'),

]