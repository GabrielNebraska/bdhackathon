from django.contrib import admin

# Register your models here.
from .models import Cargo, usuario

admin.site.register(Cargo)
admin.site.register(usuario)
