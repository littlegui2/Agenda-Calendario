from django.contrib import admin
from .models.user import User, Gestor 
admin.site.register(User)
admin.site.register(Gestor)