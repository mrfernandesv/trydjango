"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path

from pages import views
from products.views import product_create_view, dynamic_lookup_view, product_delete_view, product_list_view

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('', views.home_view, name='home'),
    path('contact/', views.contact_view),
    path('about/', views.about_view),
    path('social/', views.social_view),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('courses/', include('courses.urls')),
]
