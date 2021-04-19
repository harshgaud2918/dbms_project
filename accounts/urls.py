from django.urls import path
from . import views

urlpatterns = [
    path(route='', view=views.index, name="home"),
	path(route='login', view=views.login_as, name="login"),
    path(route='register', view=views.register, name="register"),
	path(route='login_admin', view=views.login_admin, name="login_admin"),
    path(route='login_agent', view=views.login_agent, name="login_agent"),

    path(route='agent_properties', view=views.agent_properties, name="agent_properties"),

    path(route='property_agent', view=views.display_property_agent, name="property_agent"),
    path(route='property_admin', view=views.display_property_admin, name="property_admin"),

    path(route='add_property', view=views.add_property, name="add_property"),
    path(route='add_user', view=views.add_user, name="add_user"),

    path(route='agent_dash', view=views.agent_dash, name="agent_dash"),
    #path(route='dashboard', view=views.dashboard, name="dashboard"),
    
	path(route='rent_transaction', view=views.rent_transaction, name="rent_transaction"),
    path(route='buy_sell_transaction', view=views.buy_sell_transaction, name='buy_sell_transaction')
]