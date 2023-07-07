from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'users'

urlpatterns = [
    # Login page
    path('users/login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    #Logout page
    path('logout/', views.logout_view, name='logout'),
    #The registratoin page
    path('register/', views.register, name='register'),
]
