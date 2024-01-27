from django.urls import path
from .views import test, TemperatureViews, TimeView

urlpatterns = [
    path('', test, name='test_api' ),
    path('temperature/', TemperatureViews.as_view(), name='temperature'),
    path('time/', TimeView.as_view(), name='time'),
]
