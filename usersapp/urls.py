from django.contrib import admin
from django.urls import path, include
from users import router as users_api_router
from django.conf import settings
from rest_framework import urls as rest_framework_urls

auth_api_urls = []

if settings.DEBUG:
    auth_api_urls.append(path(r'verify/', include(rest_framework_urls))) 

api_url_patterns = [
    path(r'auth/', include(auth_api_urls)),
    path(r'accounts/', include(users_api_router.router.urls))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_url_patterns)),
]
