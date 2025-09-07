from django.urls import path, include
from . import views
from dj_rest_auth.views import PasswordResetView
from .serializers import CustomPasswordResetSerializer
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('accounts/', views.UserList.as_view()),
    path('accounts/<str:pk>/', views.UserDetail.as_view()),
    path('accounts/update/<str:pk>/', views.UserUpdate.as_view()),
    path(
        'dj-rest-auth/password/reset/',
        PasswordResetView.as_view(serializer_class=CustomPasswordResetSerializer),
        name='rest_password_reset'
    ),
   
]