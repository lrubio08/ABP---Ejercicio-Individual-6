from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from .models import *
from django.contrib.auth import authenticate, login, logout





usuarios = [
    {
        'nombre' : "Gabriel",
        'apellido' : "Muñoz",
        'direccion' : "Avenida 123",
        'correo' : "gabriel_2023@example.com",
    },
    {
        'nombre' : "Jimena",
        'apellido' : "Lopez",
        'direccion' : "Calle 28",
        'correo' : "jimena.lopez@example.com",
    },
    {
        'nombre' : "Laura",
        'apellido' : "Ramirez",
        'direccion' : "pasaje b-31",
        'correo' : "laura.ramirez@example.com",
    },
    {
        'nombre' : "Carlos",
        'apellido' : "Sanchez",
        'direccion' : "Calle 12",
        'correo' : "carlos.sanchez@example.com",
    },
    {
        'nombre' : "Pedro",
        'apellido' : "Gonzalez",
        'direccion' : "Carrera 45",
        'correo' : "pedro.gonzalez@example.com",
    },
]
# Create your views here.

def index(request):
    return render(request, 'app_landing_page/index.html')

def lista_usuarios(request):
    auxiliar = {
        'usuarios': usuarios
    }
    return render(request, 'app_landing_page/usuarios.html', auxiliar)

def registrarse(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        contraseña = request.POST.get('contraseña')
        repita_contraseña = request.POST.get('repita_contraseña')
        tipo_usuario = request.POST.get('grupo')
        
        usuario_existente = CustomUser.objects.filter(username=nombre, email=correo ).exists()
        if usuario_existente:
            return render (request, 'app_landing_page/registrarse.html')
        nuevo_usuario, creado = CustomUser.objects.get_or_create(username=nombre, email=correo)
        if not creado:
            return render(request, 'app_landing_page/registrarse.html')
        nuevo_usuario.set_password(contraseña)
        nuevo_usuario.first_name = nombre
        nuevo_usuario.last_name = apellido
        if tipo_usuario == 'Vendedor':
            grupo = Group.objects.get(name= 'Vendedor')
        else:
            grupo = Group.objects.get(name= 'Cliente')
            
        nuevo_usuario.groups.add(grupo)
        nuevo_usuario.save()
        permisos_grupos = grupo.permissions.all()
        nuevo_usuario.user_permissions.set(permisos_grupos)
        nuevo_usuario.save()
        return redirect('iniciar_sesion')
    return render(request, 'app_landing_page/registrarse.html')

def iniciar_sesion(request):
    if request.method == 'POST':
        # Obtener los datos del formulario de inicio de sesión
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Autenticar al usuario
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # El inicio de sesión es exitoso, redirigir a la vista sesion_iniciada
            login(request, user)
            return redirect('sesion_iniciada')
    return render(request, 'registration/login.html')


def sesion_iniciada(request):
    user = request.user
    if user.is_authenticated and user.first_name:
        first_name = user.first_name
        return render(request, 'app_landing_page/sesion_iniciada.html', {'first_name': first_name})
    else:
        # Si el usuario no está autenticado o no tiene un nombre, redireccionar a la página de inicio de sesión
        return redirect('iniciar_sesion')
    
def cerrar_sesion(request):
    logout(request)
    return redirect('index')
