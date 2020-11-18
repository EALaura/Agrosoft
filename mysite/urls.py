"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from agrosoft.views import *

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', home, name='home'),
    path('historia', home_historia, name ='home_historia'),    
    path('mision-vision', home_misionvision, name='home_misionvision'),
    path('productos', home_productos, name='home_productos'),
    path('contactenos', home_contact, name = 'home_contact'),
    path('login', home_login, name='home_login'),
    path('salir/', home_logout, name='home_logout'),

    path('administrador/home', admi_home, name='admi_home'),
    path('usuario/home/<int:usuario_id>', usuario_home, name='usuario_home'),    
    path('administrador/usuario/agregar/', admi_agregar_usuario, name='admi_agregar_usuario'),
    path('administrador/usuario/lista/', admi_listar_usuario, name='admi_listar_usuario'),
    path('administrador/usuario/eliminar/<int:usuario_id>', admi_eliminar_usuario, name='admi_eliminar_usuario'),
    path('administrador/usuario/editar/<int:usuario_id>', admi_editar_usuario, name='admi_editar_usuario'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
