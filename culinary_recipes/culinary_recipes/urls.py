
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('culinary_recipes.auth_app.urls')),
    path('', include('culinary_recipes.recipes_app.urls')),
]
