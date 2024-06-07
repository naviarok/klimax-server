from django.urls import path
from .views import landing, consultation, success, fail

urlpatterns = [
    path('', landing, name='home'),
    path('consultation/', consultation, name='consultation'),
    path('success/', success, name='success'),
    path('fail/', fail, name='fail'),
]