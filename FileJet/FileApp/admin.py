from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(File)
admin.site.register(Chat)
admin.site.register(Message)
admin.site.register(Category)