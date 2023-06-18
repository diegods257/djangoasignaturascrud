from django.contrib import admin
from .models import Registros
# Register your models here.

class RegistrosAdmin(admin.ModelAdmin):
  readonly_fields = ('fechamatricula', ) 

admin.site.register(Registros, RegistrosAdmin)
