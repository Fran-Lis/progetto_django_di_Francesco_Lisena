from django.urls import path
from . import views

urlpatterns = [
    path('', views.diploma_search, name='diploma_search'),
    path('diploma/<int:pk>/', views.diploma_detail, name='diploma_detail'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('restricted_area', views.restricted_area, name='restricted_area'),
]