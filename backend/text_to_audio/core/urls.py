from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('converter.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
