from django.urls import path, include
from django.contrib.auth.views import (LoginView, 
                                       LogoutView,
                                       PasswordChangeView,
                                       PasswordChangeDoneView,
                                       PasswordResetView,
                                       PasswordResetDoneView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       )
from .views import RegistrationView, MyProfileView, MyProfileUpdateView
from . import views



urlpatterns =[
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'), 
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change-done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password-reset-confirm/<str:uidb64>/<str:token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('my_profile/', MyProfileView.as_view(), name='my_profile'),
    path('my_profile_update/<int:pk>', MyProfileUpdateView.as_view(), name='my_profile_update'),
    

]

