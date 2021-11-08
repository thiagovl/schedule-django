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
from core.views import views_index
from django.views.generic import RedirectView

from django.conf import settings # Necessario para configurar MEDIA_URL
from django.conf.urls.static import static # Necessario para configurar MEDIA_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views_index.index),
    path('home/', views_index.home),
    path('logout/', views_index.logout_user),
    path('index/submit', views_index.login_submit),
    path('evento/<id>', views_index.visualizar),
    path('', RedirectView.as_view(url='/home/')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
