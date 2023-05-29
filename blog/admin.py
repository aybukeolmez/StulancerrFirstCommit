from django.contrib import admin
from blog.models import Post , Category






#Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['pk','title','is_active']
    


@admin.register(Category)
class CategoryAdmim(admin.ModelAdmin):
    pass









# admin.site.register(Blog)
