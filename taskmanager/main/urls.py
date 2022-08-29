from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("", views.index),
    path("about-us",views.about),
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("const/", const, name="const"),
    path("race",views.race),
    path('reverse/', views.reverse, name='reverse'),
    path("profile", profile, name="profile"),
    path("test",views.test, name="test"),
    path("<int:pk>/", views.test_detail, name="test_detail"),
]
