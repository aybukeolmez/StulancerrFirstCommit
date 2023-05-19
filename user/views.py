from django.shortcuts import render ,redirect
from django.contrib import messages
from django.contrib.auth import login ,authenticate , logout
from django.contrib.auth.models import User
from user.models import AllUser , Freelancer
 

# Create your views here.

def login_view(request):
    
    
    context = dict()
    if request.method == "POST":
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=user_name,password=password)
        
        # if user is None:
        #     messages.warning(request,"Kullanıcı Adı veya Parola Yanlış")
        #     return render(request,'login/login.html',context)    

        
        if user is not None:
            
            login(request,user)
            messages.success(request,user_name+" "+'Başarıyla Giriş Yaptınız')
            return redirect('home_view')
            
        else:
            messages.warning(request,"Kullanıcı Adı veya Parola Yanlış")
            return render(request,'login/login.html',context)    
    
    return render(request,'login/login.html')    



def register_view(request):
    context=dict()
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        age = request.POST["age"]
        user_name = request.POST["user_name"]
        email_adress = request.POST["email_adress"]
        password = request.POST["password"]
        password_confirm = request.POST["password_confirm"]


    

        if password == password_confirm:


            
            if AllUser.objects.filter(all_user_user_name=user_name).exists(): 
                messages.warning(request,"Kullanıcı Adı Kullanılıyor")
                return render(request,'login/register.html',context)
            
            else:
                if AllUser.objects.filter(all_user_email_adress=email_adress).exists():
                    messages.warning(request,"Email Adresi Kullanılıyor") 
                    return render(request,'login/register.html',context)
                else:
                    if int(age) <=27:
                        user,created= User.objects.get_or_create(request,username=user_name,password=password)
                        user.email = email_adress
                        user.first_name = first_name
                        user.last_name = last_name
                        user.set_password(password)

                        freelancer_user, freelancer_user_created = Freelancer.objects.get_or_create(request,freelancer_user_name=user_name,freelancer_password=password)
                        freelancer_user.freelancer_first_name =first_name
                        freelancer_user.freelancer_last_name = last_name
                        freelancer_user.freelancer_email_address = email_adress
                        user.save()
                        freelancer_user.save()

                        messages.success(request,freelancer_user.freelancer_first_name+" "+freelancer_user.freelancer_last_name+" Sisteme Kaydedilniz...")
                        return render(request,'home_page/index.html')
                    
                    



                    user,created= User.objects.get_or_create(request,username=user_name,password=password)

                    user.email = email_adress
                    user.first_name = first_name
                    user.last_name = last_name
                    user.set_password(password)

                    
                    all_user , all_user_created  = AllUser.objects.get_or_create(request,all_user_user_name =user_name,all_user_password =password)
                    all_user.all_user_first_name = first_name
                    all_user.all_user_last_name = last_name
                    all_user.all_user_email_adress = email_adress
            
                    user.save()
                    all_user.save()
                    
                    messages.success(request, all_user.all_user_first_name+" "+ all_user.all_user_last_name +" Sisteme Kaydedilniz...")
                    return render(request,'home_page/index.html',context)
                    
        else:
            messages.warning(request,"Şifreler Eşleşmiyor")
            return render(request,'login/register.html',context)
        
        
        # if not created:
        #     user_login = authenticate(request,username=user_name,password=password)
        #     if user is not None:
        #         messages.success(request,"Kaydınız Bulunmaktadır.. Ana Sayfaya Yönlendiriliyorsunuz..")
        #         login(request,user_login)
        #     messages.warning(request,email_adress+" adresi sistemde kayıtlıdır.Login Sayfasına Yönlendiriliyorsunuz...")
        #     return render(request,'login/login.html')
    
    
    return render(request,'login/register.html',context)



































    # context=dict()
    # if request.method =="POST":
    #     post_info = request.POST
    #     first_name = post_info.get("first_name")
    #     last_name = post_info.get("last_name")
    #     age = post_info.get("age")
    #     user_name = post_info.get("user_name")
    #     email_adress = post_info.get("email_adress")
    #     password = post_info.get("password")
    #     password_confirm = post_info.get("password_confirm")

    #     if  len(first_name) < 6 or len(last_name) < 6 or len(user_name) < 6 or len(password) < 6 or len(email_adress) < 6:
    #         messages.warning(request,"Bilgiler En Az 6 Karakterden Oluşmalı")
    #         return render(request,'login/register.html',context)

    #     if password != password_confirm:
    #         messages.warning(request,"Lütfen Şifreleri Doğru Giriniz..")
    #         return render(request,'login/register.html',context)
    #     if int(age) >= 27:






    #         return render(request,'user_temp/user.html',context)
        
        
    #     user , created = User.objects.get_or_create(username = user_name,email=email_adress)
    #     if not created:
    #         messages.warning(request,"Daha Önce Kayıt Olmuşsunuz..")
    #         user_login = authenticate(request,username=user_name,password=password)
    #         if user is not None:
    #             messages.success(request,"Kaydınız Bulunmaktadır.. Ana Sayfaya Yönlendiriliyorsunuz..")
    #             login(request,user_login)
    #             return render(request,'home_page/index.html',context)
    #         messages.warning(request,email_adress+" adresi sistemde kayıtlıdır.Login Sayfasına Yönlendiriliyorsunuz...")
    #         return render(request,'login/login.html')  

    #     user.first_name = first_name
    #     user.last_name = last_name
    #     user.age = age
    #     user.user_name = user_name
    #     user.email_adress = email_adress
    #     user.set_password(password)

    #     profile , profile_created = Profile.objects.get_or_create(user=user)
         
    #     user.save()
    #     profile.save()

    #     messages.success(request,user.first_name+user.last_name+" Sisteme Kaydedilniz...")
    #     user_login = authenticate(request,username=user_name,password=password)
    #     login(request,user_login)
    #     return redirect('home_view')

    #return render(request,'login/register.html')
  
    
    
    


def logout_view(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız...")
    return redirect('home_view')
    
