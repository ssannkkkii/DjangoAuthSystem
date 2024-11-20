from django.urls import path
from .views import GoogleSingInView

urlpatterns = [
    path('google/', GoogleSingInView.as_view(), name='index'),
]