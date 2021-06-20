from users.views import UserLoginView, UserRegisterView
from products.views import CategoryView, ProductView
from about.views import ContactView
from order.views import OrderView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/', UserLoginView.as_view()),
    path('register/', UserRegisterView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('contacts/', ContactView.as_view({'get':'list'})),
    path('category/', CategoryView.as_view({'get':'list'})),
    path('product/', ProductView.as_view({'get':'list'})),
    path('product/<int:pk>', ProductView.as_view({'get':'retrieve'})),
    path('category/<int:pk>', CategoryView.as_view({'get':'retrieve'})),
    path('order', OrderView.as_view({'get':'list'})),
    path('order/create', OrderView.as_view({'post':'create'})),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)