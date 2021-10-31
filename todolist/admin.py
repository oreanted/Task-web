from django.contrib import admin
from .models import Task, Query


# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ("task", "done", "users")


class QueryAdmin(admin.ModelAdmin):
    list_display = ("email", "query", "date", "time")


admin.site.register(Task, TaskAdmin)
admin.site.register(Query, QueryAdmin)
