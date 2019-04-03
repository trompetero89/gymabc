from django.contrib import admin
from basic_app.models import UserProfileInfo
from basic_app.models import Menu, Alimento

# Register your models here.
admin.site.register(UserProfileInfo)

admin.site.register(Menu)
admin.site.register(Alimento)