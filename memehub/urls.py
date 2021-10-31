from django import views
from meme.views import Index
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index')
]
