from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from culinary_recipes import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('culinary_recipes.auth_app.urls')),
    path('recipes/', include('culinary_recipes.recipes_app.urls')),
    path('', include('culinary_recipes.common.urls')),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, )
