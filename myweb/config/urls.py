"""config URL Configuration

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
from django.urls import path, include
from config import views

from django.conf import settings
from django.conf.urls import url
urlpatterns = [
    path('admin/', admin.site.urls),
    #http://localhost
    path('', views.home),
    #http://localhost/address/
    path('address/', include('address.urls')),
    #http://localhost/memo/
    path('memo/', include('memo.urls')),
    path('survey/', include('survey.urls')),
    path('guestbook/', include('guestbook.urls')),
    path('member/', include('member.urls')),
    path('shop/', include('shop.urls')),
]

if settings.DEBUG: #debug 모드이면
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls))
    ]