from django.urls import path
from zustpeApp import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login/', views.loginPage,name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/',views.logoutUser,name='logout'),
]