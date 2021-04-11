from django.urls import path
from . import views

urlpatterns = [
    path(route='', view=views.index, name="home"),
	path(route='login', view=views.login, name="login"),
    path(route='register', view=views.register, name="register"),
    #path(route='dashboard', view=views.dashboard, name="dashboard"),
    
	
]