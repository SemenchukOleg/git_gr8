"""todoitapiproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from rest_framework.authtoken import views
from accounts import views as accounts_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from todoitapiproject.yasg import urlpattern as swagger_urlpatterns

urlpatterns = [  
    path('admin/', admin.site.urls),
    url(r'^api/demo/', include('demoapi.urls')),
    url(r'^api/v1/', include('apiv1.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('api-custom-token-auth/', accounts_views.CustomAuthToken.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/custom/', accounts_views.MyObtainTokenPairView.as_view(), name='token_obtain_pair')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

urlpatterns += swagger_urlpatterns