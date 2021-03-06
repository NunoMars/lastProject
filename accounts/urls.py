from django.conf.urls import url
from django.contrib.auth.views import LogoutView, LoginView
from .views import create_account_view, email_change


urlpatterns = [
    url("create_account/", create_account_view, name="create_account"),
    url("logout/", LogoutView.as_view(), name="logout"),
    url("email_change/", email_change, name="email_change"),
    url("login/", LoginView.as_view(template_name="accounts/login.html"), name="login"),
]
