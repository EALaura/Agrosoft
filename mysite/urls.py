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
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('agrosoft_web.urls', namespace='agrosoft_web')),
    path('sistema-en-linea/', include('agrosoft.urls', namespace='agrosoft')),    
    path('agrosoft_accounts/', include('agrosoft_accounts.urls', namespace='agrosoft_accounts')),
    path('accounts/api/', include('rest_auth.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 


if settings.DEBUG:  # pragma: no cover
    import debug_toolbar
    urlpatterns = [
        path(r'__debug__/', include(debug_toolbar.urls)),
        path(r'rest_framework/api-auth/', include('rest_framework.urls',
                                                  namespace='rest_framework'))
    ] + urlpatterns