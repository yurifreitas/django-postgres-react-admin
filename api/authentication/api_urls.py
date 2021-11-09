from django.conf.urls import *
from django.urls import path, include
from authentication.api_views import APILoginViewSet, APILogoutViewSet,APITokenViewSet, APIUserInfoViewSet
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('login/', APILoginViewSet.as_view(), name='api-login'),
    path('logout/', APILogoutViewSet.as_view(), name='api-logout'),
    path('token/', APITokenViewSet.as_view(), name='api-token'),
    path('user-info/', APIUserInfoViewSet.as_view(), name='api-user-info'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', ObtainAuthToken().as_view(), name='api-token-auth'),
]
