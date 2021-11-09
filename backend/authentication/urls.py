from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from authentication.views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('init/', AccountInitView.as_view(), name='account_init'),
    path('teste/',TemplateView.as_view() ),
    path('', AccountRedirectView.as_view(),
         name='account_redirect'),
    path(
        'login/', LoginView.as_view(
            template_name='registration/login.html',
        ),
        name='login',
    ),
    path(
        'logout/', LogoutView.as_view(),
        dict(
            next_page='/',
        ),
        name='logout',
    ),
    path('<slug:slug>/edit/',
         AccountUpdateView.as_view(), name='account_edit'),
    path('<slug:slug>/', AccountDetailView.as_view(),
         name='account_detail'),
]
