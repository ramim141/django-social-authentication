from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication_app.urls')), 
    path('social/', include('social_django.urls', namespace='social')),
]