from django.contrib import admin

# Register your models here.
from .models import Cargo, funcionario

admin.site.register(Cargo)
admin.site.register(funcionario)