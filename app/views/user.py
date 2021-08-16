from rest_framework import viewsets,permissions
from app.models import User
from app.serializers.user import RegisterSerializer

class RegisterAPI(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = User.objects
    serializer_class = RegisterSerializer