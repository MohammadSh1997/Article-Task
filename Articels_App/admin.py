from django.contrib import admin
from Articels_App.models import Sys_user , Comment , Article
# Register your models here.
admin.site.register(Sys_user)
admin.site.register(Article)
admin.site.register(Comment)
