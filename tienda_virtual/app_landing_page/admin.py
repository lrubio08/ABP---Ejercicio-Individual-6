from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Configurar el modelo CustomUser en el sitio de administración
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Personaliza los campos que se mostrarán en la lista de usuarios del sitio de administración
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']

# Registrar el modelo personalizado CustomUser en el sitio de administración
admin.site.register(CustomUser, CustomUserAdmin)
