from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("login/", views.login_page, name="login"),
    path("register/", views.register_page, name="register"),
    path("logout/", views.logout_page, name="logout"),
    path("add/", views.add_product, name="add_product"),
    path("delete/<str:pk>/", views.delete_product, name="delete_product"),
]