from django.urls import path
from . import views

urlpatterns = [
    # path('signup/',views.signup, name='signup'),
    # path('login/', views.login_view, name='login'),
    # path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('',views.frontpage,name='frontpage'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),  # Assuming you have a home view.
    path('client/register/', views.client_register, name='client_register'),
    path('client/login/', views.client_login, name='client_login'),
    path('client/home/', views.client_home, name='client_home'),

]
