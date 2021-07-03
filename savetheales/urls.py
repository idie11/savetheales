from django.conf.urls import url
from users.views import UserLoginView, UserRegisterView
from products.views import CategoryView, ProductView
from about.views import ContactView
from order.views import OrderView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="aidaitazabekova@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/v1/login/', UserLoginView.as_view()),
    path('api/v1/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/register/', UserRegisterView.as_view()),
    path('contacts/', ContactView.as_view({'get':'list'})),
    path('category/', CategoryView.as_view({'get':'list'})),
    path('product/', ProductView.as_view({'get':'list'})),
    path('product/<int:pk>', ProductView.as_view({'get':'retrieve'})),
    path('category/<int:pk>', CategoryView.as_view({'get':'retrieve'})),
    path('order/', OrderView.as_view({'get':'list'})),
    path('order/create', OrderView.as_view({'post':'create'})),
    path('order/<int:pk>', OrderView.as_view({'get':'retrieve'})),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)