from django.urls import path
from accounts import views

app_name='accounts'

urlpatterns=[
    path('Register',views.register,name='register'),
]
