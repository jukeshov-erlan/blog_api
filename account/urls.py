from django.urls import path
from .views import RegistrationView, ActivationView, LoginView, LogoutView, ChangePasswordVIew, ForgotPasswordView, ForgotPasswordCompleteView

urlpatterns = [
    # path('', SomeView.as_view()),
    path('register/', RegistrationView.as_view()),
    path('activate/', ActivationView.as_view()), 
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('change_password/', ChangePasswordVIew.as_view()),
    path('forgot_password/', ForgotPasswordView.as_view()),
    path('forgot_password_complete/', ForgotPasswordCompleteView.as_view())
]
