from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    path("private_page_1/", views.private_page_1, name="private_page_1",),
    path("private_page_2/", views.private_page_2, name="private_page_2",),
    path("login", auth_views.LoginView.as_view(), name = "login",),
    path("logout", auth_views.LogoutView.as_view(), name = "logout",),
    path("password_change",auth_views.PasswordChangeView.as_view(success_url = "password_change_done"), name = "password_change",),
    path("password_change_done",auth_views.PasswordChangeDoneView.as_view(), name = "password_change_done",),
    path("password_reset", auth_views.PasswordResetView.as_view(success_url = "password_reset_done",), name = "password_reset",),
    path("password_reset_done", auth_views.PasswordResetDoneView.as_view(), name = "password_reset_done",),
    path("password_reset_confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(success_url = "/accounts/password_reset_complete"), name="password_reset_confirm"),
    path("password_reset_complete", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),


]