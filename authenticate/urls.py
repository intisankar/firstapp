from django.urls import path
from . import views # for multiple views 

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
    path('editprofile/',views.edit_profile,name='editprofile'),
    path('change_password/',views.change_password,name='change_password'), 

]
