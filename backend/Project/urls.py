from django.contrib import admin
from django.urls import path, include
from .views import ServerTest

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/convert/', include('convert.urls')),
    path('api/convert/units/', include('units.urls')),
    path('test/', ServerTest.as_view()),
    path("__debug__/", include("debug_toolbar.urls")),
]
