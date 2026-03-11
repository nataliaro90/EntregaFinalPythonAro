from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.admin_url if hasattr(admin.site, 'admin_url') else admin.site.urls),
    path('', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
]

# Esto permite ver las imágenes en el navegador durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Personalización del Admin en tonos Rosa
from django.contrib import admin

admin.site.site_header = "Administración de Mi Blog Rosa ✨"
admin.site.site_title = "Blog Naty Admin"
admin.site.index_title = "Panel de Control 🌸"