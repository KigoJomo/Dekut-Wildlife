from django.urls import path
from . import views

urlpatterns = [
    path('dekut_env/', views.dekut_env, name='dekut_env')
]
