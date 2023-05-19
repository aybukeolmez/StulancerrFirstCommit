from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from blog.models import Post , Category
from blog.form import PostModelForm

from user.models import Freelancer , AllUser




# Create your views here.

# HOME PAGE DEF
def home_view(request):
    freelancer_list =Freelancer.objects.order_by("-freelancer_first_name")
    
    context = dict(
        freelancer_list = freelancer_list
    )
    
    # latest_freelancer_list = Freelancer.objects.order_by("-register_date")[:5]
    # context = {"latest_freelancer_list": latest_freelancer_list}

    return render(request,'home_page/index.html',context)


# CATEGORY DEF
# def category_view(request,category_slug):
    # category = get_object_or_404(Cetagory,slug = category_slug)
    # categories = Cetagory.objects.all().order_by('title')
    # posts = Post.objects.all().order_by('-created_at',category=category)


    # context =dict(
    #     category = category,
    #     categories = categories,
    #     posts = posts,
    # )
    
    
    # latest_freelancer_list = Freelancer.objects.order_by("-register_date")[:5]
    # context = {"latest_freelancer_list": latest_freelancer_list}

    # return render(request,'home_page/index.html',context)

# PAGE DEF
def ceviri_view(request):
    freelancer_list =Freelancer.objects.order_by("-freelancer_first_name")
    posts = Post.objects.all()
    context =dict(
        posts = posts,
        freelancer_list = freelancer_list
    )
    return render(request,'layouts/ceviri.html',context)

def grafik_view(request):
    freelancer_list =Freelancer.objects.order_by("-freelancer_first_name")
    posts = Post.objects.all()
    context =dict(
        posts = posts,
        freelancer_list = freelancer_list
    )
    return render(request,'layouts/grafik.html',context)


def muzik_view(request):
    freelancer_list =Freelancer.objects.order_by("-freelancer_first_name")
    posts = Post.objects.all()
    context =dict(
        posts = posts,
        freelancer_list = freelancer_list
    )
    return render(request,'layouts/muzik.html',context)


def reklam_view(request):
    freelancer_list =Freelancer.objects.order_by("-freelancer_first_name")
    posts = Post.objects.all()
    context =dict(
        posts = posts,
        freelancer_list = freelancer_list
    )
    return render(request,'layouts/reklam.html',context)


def video_view(request):
    freelancer_list =Freelancer.objects.order_by("-freelancer_first_name")
    posts = Post.objects.all()
    context =dict(
        posts = posts,
        freelancer_list = freelancer_list
    )
    return render(request,'layouts/video.html',context)


def yazilim_view(request):
    freelancer_list =Freelancer.objects.order_by("-freelancer_first_name")
    posts = Post.objects.all()
    context =dict(
        posts = posts,
        freelancer_list = freelancer_list
    )
    return render(request,'layouts/yazilim.html',context)



def yonetim_view(request):
    freelancer_list =Freelancer.objects.order_by("-freelancer_first_name")
    posts = Post.objects.all()
    context =dict(
        posts = posts,
        freelancer_list = freelancer_list
    )
    return render(request,'layouts/yonetim.html',context)







# def addBlog_view(request):
#     form = PostModelForm
#     context ={
#         'form':form
#      }
#     return render(request,'layouts/addblog.html',context)


# FREELANCER PAGES

def  freelancer_detail(request,freelancer_id):  # Normalde FREELANCER ID ye göre gelmesi lazım.Düzeltilcek
    freelancer_detail = Freelancer.objects.filter(pk=freelancer_id)
    context = dict(
        freelancer_detail = freelancer_detail
    )
    return render(request, "freelancer_temp/fre_for_user.html",context)

# def freelancer_detail(request, freelancer_id):
#     freelancer = get_object_or_404(Freelancer, pk=freelancer_id)
#     return render(request, "freelancer_temp/fre_for_user.html", {"freelancer": freelancer})


def freelancer_profil_duzenle(request):
    context = {

    }
    return render(request,'freelancer_temp/fre_profil_duzenle.html')

def freelancer_is(request):
    posts = Post.objects.order_by('-created_at')
    context = dict(
        posts = posts
    )
        
    
    return render(request,'freelancer_temp/freelancer_is.html')

# POST YÜKLEME
@login_required(login_url='user:login_view')
def freelancer_post_card(request):
    form = PostModelForm()
    context = dict(
        form = form
    )
    if request.method == 'POST':
        form = PostModelForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            f = form.save(commit=False)
            f.free_user = request.user
            f.save()
            messages.success(request,'Postunuz Kaydedilmiştir')
    return render(request,'freelancer_temp/freelancer_post_card.html',context)





def freelancer_post(request):
    context={
        
    }
    return render(request,'freelancer_temp/freelancer_post.html',context)


def freelancer_profil(request):
    context = {

    }
    return render(request,'freelancer_temp/freelancer_profil.html')


# USER PAGES



def user_profil(request):
    context = {
        
    }
    return render(request,'user_temp/user.html')

def user_profil_duzenle(request):
    context = {

    }
    return render(request,'user_temp/user_profil_duzenle.html')
