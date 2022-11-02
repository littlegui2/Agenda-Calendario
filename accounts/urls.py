from django.urls import path

from accounts import views
from .views.signup import GSignUpView
app_name = "accounts"


urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("signin/", views.SignInView.as_view(), name="signin"),
    path("gsignup/", GSignUpView.as_view(), name="gsignup"),
    path("signout/", views.signout, name="signout"),
]
