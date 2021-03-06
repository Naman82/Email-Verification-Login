from django.urls import path
from . import views

urlpatterns=[
    path('',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('success/',views.success,name='success'),
    path('token/',views.token_send,name='token_send'),
    path('welcome/',views.welcome,name='welcome'),
    path('verify/<auth_token>',views.verify,name='verify'),
    path('error/',views.error,name='error'),
]