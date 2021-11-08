from django.contrib import admin
from django.urls import path
from meme.views import Index

from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', Index.as_view(), name='index'),
    
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
