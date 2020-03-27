from django.urls import path
from . import views


urlpatterns = [
    path('pin/',views.get_pin),
    path('result/',views.post_pin)
]
