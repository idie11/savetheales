from django.contrib.auth import authenticate
from rest_auth.models import TokenModel
from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer, UserLoginSerializer
# from .permissions import IsStaffOrCreateUser, UserPermissionOrReadOnly
 
class UserRegisterView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    # permission_classes = (IsStaffOrCreateUser, UserPermissionOrReadOnly)
 
class UserLoginView(GenericAPIView):
    serializer_class = UserLoginSerializer
 
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.data.get('username')
        password = serializer.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            token = TokenModel.objects.get(user=user)
            return Response({​​​​​​​​'key': token.key}​​​​​​​​, status=status.HTTP_201_CREATED)
        return Response('invalid login', status=status.HTTP_401_UNAUTHORIZED)

