from django.urls import path
from .views import register_view, login_view, logout_view, verify_otp

app_name = 'userapp'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('verify-otp/', verify_otp, name='verify_otp'),
]


