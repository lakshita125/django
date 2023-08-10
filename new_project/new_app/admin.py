from django.contrib import admin
from  new_app.models import Students,classroom,teachers,marks

# Register your models here.
admin.site.register(Students)
admin.site.register(classroom)
admin.site.register(teachers)
admin.site.register(marks)
