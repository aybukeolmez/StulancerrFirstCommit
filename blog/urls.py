from django.contrib import admin
from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    
    #PAGES
    path('',views.home_view,name='home_view'),
    


    path('ceviri/',views.ceviri_view,name='ceviri_vieww'),
    path('grafik/',views.grafik_view,name='grafik_view'),
    path('muzik/',views.muzik_view,name='muzik_view'),
    path('reklam/',views.reklam_view,name='reklam_view'),
    path('video/',views.video_view,name='video_view'),
    path('yazilim/',views.yazilim_view,name='yazilim_view'),
    path('yonetim/',views.yonetim_view,name='yonetim_view'),
    
    #DASHBOARD
    #Freelancer
    path('kontrolpanel/',views.freelancer_profil,name='freelancer_profil'),
    path('postblog/',views.freelancer_post_card,name='freelancer_post_card'),
    path('profilduzenle/',views.freelancer_profil_duzenle,name='freelancer_profil_duzenle'),
    path('profilis/',views.freelancer_is,name='freelancer_is'),
    path('profilpost/',views.freelancer_post,name='freelancer_post'),
    
    #User
    path('userprofil/',views.user_profil,name='user_profil'),
    path('userProfilduzenle/',views.user_profil_duzenle,name='user_profil_duzenle'),



    #PROFİL - FREELANCER
    path('freelancerdetail/<int:freelancer_id>/',views.freelancer_detail,name='freelancer_detail')
    # path("<int:freelancer_id>/",views.freelancer_detail, name="freelancer_detail"),
    
    
    
]