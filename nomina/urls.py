from django.urls import path
from knox import views as knox_views
from . import views

urlpatterns = [
    path('registro/', views.registro),
    path('login/', views.login),
    path('logout/', knox_views.LogoutView.as_view()),
    path('logoutall/', knox_views.LogoutAllView.as_view())
]