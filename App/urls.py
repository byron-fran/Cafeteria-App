
from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Core.urls')),
    path('services', include('Services.urls')),
    path('blog/', include('Blog.urls')),
    path('page/', include('pages.urls')),
    path('contact/', include('Contact.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)