from django.contrib.auth import authenticate, get_user_model
from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer, UserLoginSerializer
from .permissions import UserPermissionOrReadOnly
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny


User = get_user_model()


class UserRegisterView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = (UserPermissionOrReadOnly, )
 
class UserLoginView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer
 
    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     username = serializer.data.get('username')
    #     password = serializer.data.get('password')
    #     user = authenticate(request, username=username, password=password)
    #     if user:
    #         token = TokenModel.objects.get(user=user)
    #         return Response({'key': token.key}, status=status.HTTP_201_CREATED)
    #     return Response('invalid login', status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(request, username=serializer.data.get('username'), password=serializer.data.get('password'))
        if user:
            refresh = RefreshToken.for_user(user)
            return Response(data={
                'refresh': str(refresh),
                'access': str(refresh.access_token)}
            )
        return Response(
            data={'message': 'username or password is incorrect'},
            status=status.HTTP_401_UNAUTHORIZED
        )