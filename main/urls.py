"""main URL Configuration

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
from django.urls import path,include
from teachers import views
from django.views.generic.base import TemplateView # new


urlpatterns = [
    path('admin/', admin.site.urls),
    path('teachers/', include('django.contrib.auth.urls')),
    path('teachers/', include('teachers.urls')),
    path('', include('teachers.urls')),
    path('core/', include('core.urls')),
    # path('signup/',views.SignupPage,name="signup"),
    path('login/',views.login_view, name="login"),
    path('home/',views.home, name="home"),
    path('home/templates/deptcse/',views.deptcse_view,name="dept-cse"),
    path('', TemplateView.as_view(template_name='myhome.html'), name='myhome'), # ne
    path('teachers/mylogin/',include('django.contrib.auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('logout/',views.LogoutPage,name='logout'),
]
