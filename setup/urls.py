from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, permissions
from api_loja.api import viewsets
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title= "Financeiro API",
        default_version='v1',
        description= "Sistema para amostra de lojas",
        terms_of_service="https://www.google.com/policies/terms",
        contact=openapi.Contact(email="contato@yaishe.com.br"),
        license=openapi.License(name="Free"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

route = routers.DefaultRouter()
route.register(r'cliente', viewsets.ClienteViewsets, basename="Cliente")
route.register(r'mostruario', viewsets.MostruarioViewsets, basename="Mostruario")
route.register(r'carrinho', viewsets.CarrinhoViewsets, basename="Carrinho")
route.register(r'itemcarrinho', viewsets.ItemCarrinhoViewsets, basename="Item Carrinho")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),

]
urlpatterns += [
    path('swaggerjson/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]