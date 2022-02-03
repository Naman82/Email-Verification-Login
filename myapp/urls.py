from django.urls import path
from . import views

urlpatterns=[
    path('',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('success/',views.success,name='success'),
    path('token/',views.token_send,name='token_send'),
]