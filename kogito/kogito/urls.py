"""kogito URL Configuration

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
from django.urls import path
from kogitos import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('search/', views.search, name='search'),
    path('more/', views.more, name='more'),
    path('mylibrary__playlist/', views.mylibrary__playlist, name='mylibrary__playlist'),
    path('mylibrary__book/', views.mylibrary__book, name='mylibrary__book'),
    path('mylibrary__people/', views.mylibrary__people, name='mylibrary__people'),
    path('bookmark/', views.bookmark, name='bookmark'),
    path('ashlee_vance_book/', views.ashlee_vance_book, name='ashlee_vance_book'),
    path('ashlee_vance_book_ch1/', views.ashlee_vance_book_ch1, name='ashlee_vance_book_ch1'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update_application/', views.update_application, name='update_application'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  #업로드한 파일이 다운받을 수 있게 url로 제공됨
