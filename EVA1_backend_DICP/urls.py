"""
URL configuration for EVA1_backend_DICP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from DICP_App1_v1 import views
from DICP_App2_v1 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('view1/', views.view1),
    path('view2/', views.view2),
    path('admin/', admin.site.urls),
    path("v1/", views.v1),
    path("v2/", views.v2),
]


