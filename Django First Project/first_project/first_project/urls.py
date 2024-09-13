"""
URL configuration for my_first_project project.

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
from django.urls import re_path
from first_app import views

urlpatterns = [
    re_path(r'^$',views.index,name='index'),             # domain
    re_path(r'^form/',views.form_view,name='form'),     # domain/form/
    re_path(r'^about/',views.about,name='about'),        # domain/about/
    re_path('admin/', admin.site.urls),                  # domain/admin/
]
