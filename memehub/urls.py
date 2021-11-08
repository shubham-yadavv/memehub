from django.contrib import admin
from django.urls import path
from meme.views import PostsView, RandomView

from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('admin', admin.site.urls),
    path('', PostsView.as_view(),  name="posts"),
    path('random', RandomView.as_view(),  name="random"),
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)