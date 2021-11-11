"""schedule URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from core.views import view_index, view_home, view_signup, view_crud
from django.views.generic import RedirectView

from django.conf import settings # Necessario para configurar MEDIA_URL
from django.conf.urls.static import static # Necessario para configurar MEDIA_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', view_index.index),
    path('home/', view_home.home),
    path('logout/', view_signup.logout_user),
    path('index/login', view_signup.login_user),
    path('evento/<id>', view_crud.visualizar),
    path('evento/adicionar/', view_home.adicionar),
    path('evento/editar/', view_crud.editar),
    path('salvar', view_crud.salvar_ediar),
    path('', RedirectView.as_view(url='/home/')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
