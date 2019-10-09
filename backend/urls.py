from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from backend import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)