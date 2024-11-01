"""
URL configuration for dressup_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.http import HttpResponse
from dressup_app import views
from django.conf import settings
from django.conf.urls.static import static
# Fonction simple pour afficher un message sur la page d'accueil
def home_view(request):
    return HttpResponse("Bienvenue sur la page d'accueil !")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),  # URL de la page d'accueil
    path('dressup_app/', include('dressup_app.urls')),  # Include the app's URLs that are defined in dressup_app/urls.py
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
