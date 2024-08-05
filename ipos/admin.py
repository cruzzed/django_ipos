from django.contrib import admin
from .models import TblUser


@admin.register(TblUser)
class TblUserAdmin(admin.ModelAdmin):
    pass