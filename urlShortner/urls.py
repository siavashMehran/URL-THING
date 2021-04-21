
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from urlShortner import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),



    
    path('', include('urlReciever.urls')),
]



urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
