from django.contrib import admin

# Register your models here.
from .models import Cargo, Usuario

admin.site.register(Cargo)
admin.site.register(Usuario)
