from django.urls import path
from apps.usuario import views

app_name = 'usuario'
urlpatterns = [
    path('login', views.loginView, name='login'),
    path('logout',views.logoutView, name='logout')
]

