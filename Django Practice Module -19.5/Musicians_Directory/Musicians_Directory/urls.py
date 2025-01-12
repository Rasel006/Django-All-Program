from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('author.urls')),
    path('musician/', include('musician.urls')),
    path('album/', include('album.urls')),
]