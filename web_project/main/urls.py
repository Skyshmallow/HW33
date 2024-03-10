from django.urls import path
from django.contrib import admin
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('admin', admin.site.urls)
]
