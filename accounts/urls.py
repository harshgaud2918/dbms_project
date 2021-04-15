from django.urls import path
from . import views

urlpatterns = [
    #path(route='', view=views.index, name="home"),
	path(route='login', view=views.login, name="login"),
    path(route='register', view=views.register, name="register"),
	path(route='login_admin', view=views.login_admin, name="login_admin"),
    path(route='login_agent', view=views.login_agent, name="login_agent")
]