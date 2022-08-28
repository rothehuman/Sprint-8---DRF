"""nueva_api URL Configuration

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
from django.urls import path, include
from libros import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('libros.urls')),

    #path('admin/', admin.site.urls),
    #path('', views.api_root),
    #path('libros/', views.LibroLists.as_view(), name='libros-list'),
    #path('libros/<int:pk>/', views.LibroDetails.as_view(), name='libro-detail'),
    #path('users/', views.UserList.as_view(), name='user-list'),
    #path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),

    #en api ponemos nuestro endpoint
    #path('api/libros/', LibroLists.as_view()),
    #path('api/libros/<int:pk>/',LibroDetails.as_view()),
    #path('api/users/', UserList.as_view()),
    #path('api/users/<int:pk>/', UserDetail.as_view())
]
