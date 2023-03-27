from django.contrib import admin
from .models import Table1
# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display =("firstname","lastname","deathyear","joined_date",)
admin.site.register(Table1,MemberAdmin)
