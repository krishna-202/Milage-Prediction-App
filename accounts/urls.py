from django.urls import path
from accounts import views

app_name='accounts'

urlpatterns=[
    path('Register',views.register,name='register'),
    path('Login',views.login,name='login'),
    path('Logout',views.logout,name='logout'),
]
