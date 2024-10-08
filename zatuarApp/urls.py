"""zatuarApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from Home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('empresa/', empresa),
    path('linea/', linea),
    path('linea/<slug:lineaa>/', linea_cate),
    path('productos/', producto),
    path('productos/<int:id>/', producto_cate),
    path('producto/<int:id>/', producto_id),
    path('clientes/', clientes),
    path('clientes/<int:id>/', clientes_id),
    path('blog/', blog),
    path('post/<int:n>/', post),
    path('post/<int:n>/', post),
    path('contacto/', contacto),
    path('error/', error404),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
