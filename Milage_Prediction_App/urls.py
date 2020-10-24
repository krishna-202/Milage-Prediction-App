from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('predict_milage',views.predict_milage,name='predict_milage'),

]
