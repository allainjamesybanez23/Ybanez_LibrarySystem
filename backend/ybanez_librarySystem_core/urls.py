"""
URL configuration for ybanez_librarySystem_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
<<<<<<< HEAD:backend/backend/backend/ybanez_librarySystem_core/urls.py
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
=======
<<<<<<< HEAD
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
=======
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from library.views import StudentView, BookView, TransactionView

# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'students', StudentView)
router.register(r'books', BookView)
router.register(r'transactions', TransactionView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
>>>>>>> dec0a3d8a5ca3284071ba889f30e548eb12d5a7c
>>>>>>> b7a08b98aa31bb42367216a70a867d88a62950e9:backend/ybanez_librarySystem_core/urls.py
]
