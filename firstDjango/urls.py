"""firstDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from .views import home_view
# 從app01 views下導入
from app01 import views

urlpatterns = [
    # path('',home_view),
    # path('admin/', admin.site.urls),
    # www.xxx.com/index/ 好像是首頁 -->持行函數
    # path('index/',admin.site.urls)
    path('index/',views.index),
    path('user/list/',views.user_list),
    path('user/add/',views.user_add),
    path('something/',views.something),
    path('login/',views.login),
    path('orm/',views.orm),
    ##案例:用戶管理+連接API
    path('info/list/',views.info_list),
    path('info/add/',views.info_add)
]
