"""memory_management1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from hello1 import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('signup/',views.sign_up,name='signup'),
    path('login/',views.log_in,name='login'),
    path('logout/',views.log_out,name='logout'),
    path('addshow/',views.add_show,name='addshow'),
    path('updatebook/<int:id>',views.updatebook,name='updatebook'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('books/',views.user_books,name='books'),
    path('api/',include('hello1.api.urls'))      # This is api url which is created in hello1 folder
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   # This settings for image upload from the data base
