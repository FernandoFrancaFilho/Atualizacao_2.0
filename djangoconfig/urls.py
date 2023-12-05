from django.contrib import admin
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.urls import path, include
from userapp.views import InnderJoinCreateView, InnderJoinCreateView2


urlpatterns = [
    path('api/instances/<int:id>/', InnderJoinCreateView.as_view(), name="instances"), # Inner Join Criança
    path('api/instances2/<int:id>/', InnderJoinCreateView2.as_view(), name="instances"), # Inner Join Consulta
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('', include('userapp.urls')),
]