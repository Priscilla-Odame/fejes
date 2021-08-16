from django.urls import path, include
from app.views.user import RegisterAPI
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'register', RegisterAPI, 'signup')

urlpatterns = [
    path('api/', include(router.urls)),
]