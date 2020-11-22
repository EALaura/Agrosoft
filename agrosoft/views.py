from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from .forms import *
from django.contrib import messages
from django.urls import reverse
from .models import *
from django.db.models import Q

# Views de la página web e inicio de sesión.
# Checks if the user is user or admin type
def system_home(request):	
	if request.user.groups.filter(Q(name='Administrador') | Q(name='Personal')).exists(): 
		return redirect(reverse('agrosoft:adminhome'))
	else:
		return redirect(reverse('agrosoft_accounts:login'))

# Views de la Gestión de Lotes
def listar_lotes(request):
    title = 'Lista de convocatorias'
    context = {
		"title": title		
	}
    return render(request, 'agrosoft/lotes/listar_lotes.html', context)



# Views de la Gestión de Usuarios
# Listar Usuarios registrados
def listar_usuario(request):
    usuario = User.objects.filter(groups__name='Administrador')
    context = {
        'usuario': usuario,
    }
    return render(request, 'agrosoft/usuarios/listar_usuarios.html', context)

# Agregar un nuevo Usuario
def agregar_usuario(request):
    groups = Group.objects.exclude(name='Administrador').exclude(name='Personal')
    
    if request.method == 'POST':
        formulario = UsuarioFormulario(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            grupo = Group.objects.get(name='Administrador')
            usuario.groups.add(grupo)
            messages.info(request,'Usuario registrado con éxito')
            return redirect(reverse('agrosoft:listarusuarios'))
    else:
        formulario = UsuarioFormulario()
    context = {
        'formulario': formulario
    }
    return render(request, 'agrosoft/usuarios/agregar_usuario.html', context)

# Mostrar detalle de un usuario
def detalle_usuario(request, usuario_id):
	title = 'Detalle de usuario'
	usuario = User.objects.get(id = usuario_id)

	return render(request, 'agrosoft/usuarios/detalle_usuario.html', locals())

# Editar un Usuario
def editar_usuario(request, usuario_id):
    usuario = User.objects.get(id = usuario_id)
    if request.method == 'GET':
        form = UsuarioFormulario(instance = usuario)
        context = {
            'form': form
        }
    else:
        form = UsuarioFormulario(request.POST, instance = usuario)
        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
            messages.info(request, 'Usuario actualizado')
            return redirect('agrosoft:listarusuarios')
    return render(request, 'agrosoft/usuarios/editar_usuario.html', context)

# Eliminar un Usuario registrado
def eliminar_usuario(request, usuario_id):
    usuario = User.objects.get(id = usuario_id)
    usuario.delete()
    messages.info(request, 'Usuario eliminado con éxito')
    return redirect('agrosoft:listarusuarios')

# Views de la Gestión de Cultivos
# Listar Cultivos registrados
def listar_cultivo(request):
    query_set = Cultivo.objects.all()
    cultivos = reversed(list(query_set))
    context = {
        'cultivos': cultivos,        
    }
    return render(request, 'agrosoft/cultivos/listar_cultivos.html', context)      

# Agregar un nuevo Cultivo
def agregar_cultivo(request):    
    
    if request.method == 'POST':
        formulario = CultivoFormulario(request.POST)
        if formulario.is_valid():
            cultivo = formulario.save()                        
            messages.info(request,'Cultivo registrado con éxito')
            return redirect(reverse('agrosoft:listarcultivos'))
    else:
        formulario = CultivoFormulario()
    context = {
        'formulario': formulario
    }
    return render(request, 'agrosoft/cultivos/agregar_cultivo.html', context)

# Mostrar detalle de un cultivo
def detalle_cultivo(request, cultivo_id):
	title = 'Detalle de Cultivo'
	cultivo = Cultivo.objects.get(id = cultivo_id)

	return render(request, 'agrosoft/cultivos/detalle_cultivo.html', locals())

# Editar un Cultivo
def editar_cultivo(request, cultivo_id):
    cultivo = Cultivo.objects.get(id = cultivo_id)
    if request.method == 'GET':
        form = CultivoFormulario(instance = cultivo)
        context = {
            'form': form
        }
    else:
        form = CultivoFormulario(request.POST, instance = cultivo)
        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
            messages.info(request, 'Cultivo actualizado')
            return redirect('agrosoft:listarcultivos')
    return render(request, 'agrosoft/cultivos/editar_cultivo.html', context)

# Eliminar un Cultivo registrado
def eliminar_cultivo(request, cultivo_id):
    cultivo = Cultivo.objects.get(id = cultivo_id)
    cultivo.delete()
    messages.info(request, 'Cultivo eliminado')
    return redirect('agrosoft:listarcultivos')
