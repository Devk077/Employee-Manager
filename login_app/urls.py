from django.urls import path,include
from . import views

app_name = 'login_app'

urlpatterns = [
    path('',views.profile_page,name='profile_page'),
    path('special/',views.special,name='special'),
    path('login/',views.loginUser,name='login'),
    path('logout/',views.logoutUser,name='logout'),
]