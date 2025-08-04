"""
URL configuration for Newsportal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from Media import views
from Newsportal import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Homepage),
    path('homepage/', views.Homepage,name="homepage"),
    path('header/', views.header,name="header"),
    path('category/', views.category_page,name="category"),
    path('fashion/', views.Fashion,name="fashion"),
    path('lifestyle/', views.lifestyle_page,name="lifestyle"),
    path('travel/', views.Travel,name="travel"),
    path('sports/', views.Sports,name="sports"),
    path('technology/', views.Technology,name="technology"),
    path('details/<int:id>', views.Details,name="details"),
    path('about/', views.About,name="about"),
    path('latestnews/', views.LatestNews,name="latestnews"),
    path('contact/', views.Contact,name="contact"),
    path('elements/', views.Elements,name="elements"),
    path('login/', views.login_page,name="login"),
    path('register/', views.register_page,name="register"),
    path('blog/', views.Blog_page,name="blog"),
    path('blog_details/<int:id>', views.Blog_Details,name="blog_details"),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)