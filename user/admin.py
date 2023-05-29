from django.contrib import admin
from user.models import AllUser , Freelancer
from django.contrib.auth.models import User


# Register your models here.
class AllUserAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'all_user_first_name',
        'all_user_last_name',
        'all_user_user_name',
        'all_user_email_adress',
        ]
    list_display_links =[
        'pk',
        'all_user_first_name',
        'all_user_last_name',
        'all_user_user_name',
        'all_user_email_adress',
        ]
    

class FreelancerAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'freelancer_first_name',
        'freelancer_last_name',
        'freelancer_user_name',
        'freelancer_email_address',
        ]  
    list_display_links =[
        'pk',
        'freelancer_first_name',
        'freelancer_last_name',
        'freelancer_user_name',
        'freelancer_email_address',
    ]
admin.site.register(AllUser,AllUserAdmin)
admin.site.register(Freelancer,FreelancerAdmin)



