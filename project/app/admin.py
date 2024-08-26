from django.contrib import admin
from .models import Students,Teacher,Complaints
# Register your models here.


admin.site.register(Students)
admin.site.register(Teacher)
admin.site.register(Complaints)