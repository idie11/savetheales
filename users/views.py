from django.contrib.auth import authenticate, get_user_model
from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response
from .serializers import UserProfileSerializer, UserRegisterSerializer, UserLoginSerializer, ReviewSerializer
from .permissions import UserPermissionOrReadOnly
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from .models import Review


User = get_user_model()


class UserRegisterView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = (UserPermissionOrReadOnly, )

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.filter(username=serializer.data.get('username')).first()
        user = authenticate(request, username=serializer.data.get('username'), password=serializer.data.get('password'))
        
        if not user:
            user = User.objects.create(username=serializer.data.get('username'))
            user.set_password(serializer.data.get('password'))
            refresh = RefreshToken.for_user(user)
            return Response(data={
                'refresh': str(refresh),
                'access': str(refresh.access_token)}
            )
        return Response(
            data={'message': 'username already exist'},
            status=status.HTTP_401_UNAUTHORIZED
        )
 
class UserLoginView(GenericAPIView):
    permission_classes =(UserPermissionOrReadOnly, )
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


class ReviewView(ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    lookup_field = 'pk'
    permission_classes = (AllowAny, )



class UserProfileView(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()
    lookup_field = 'pk'
    permission_classes = (UserPermissionOrReadOnly, )