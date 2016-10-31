from django.contrib import admin
from lists.models import Task, Group_task
# Register your models here.
class MyModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Task, MyModelAdmin)
admin.site.register(Group_task, MyModelAdmin)