from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.login_user, name="login_user"),
    path("logout/", views.logout_user, name="logout_user"),
    path("update-user", views.update_user, name="update_user"),
    path("create-thought", views.create_thought, name="create_thought"),
    path("update-thought/<int:pk>", views.update_thought, name="update_thought"),
    path("delete-thought/<int:pk>", views.delete_thought, name="delete_thought"),
]
