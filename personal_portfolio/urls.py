"""
URL configuration for personal_portfolio project.

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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("projects.urls")),
    path("projects/", include("projects.urls")),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
'''
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import project_index  # Import the project_index view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", project_index, name='home'),  # Use project_index at root URL
    path("projects/", include("projects.urls")),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
'''