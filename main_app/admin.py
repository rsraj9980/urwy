from django.contrib import admin
from .models import Task, Bid, Category

# Register your models here.

admin.site.register(Task)
admin.site.register(Bid)
admin.site.register(Category)

