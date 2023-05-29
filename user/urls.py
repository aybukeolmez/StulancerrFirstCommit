from django.contrib import admin
from django.urls import path
from . import views

app_name = "user"

urlpatterns = [ 
    path('register/',views.register_view,name='register_view'),
    path('login/',views.login_view,name='login_view'), 
    path('logout/',views.logout_view,name='logout_view'),


]