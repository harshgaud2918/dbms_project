from django.urls import path
from . import views

urlpatterns = [
    path(route='', view=views.index, name="home"),
	path(route='login', view=views.login_as, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path(route='register', view=views.register, name="register"),
	path(route='login_admin', view=views.login_admin, name="login_admin"),
    path(route='login_agent', view=views.login_agent, name="login_agent"),

    path(route='agent_properties', view=views.agent_properties, name="agent_properties"),

    path(route='property_agent', view=views.display_property_agent, name="property_agent"),
    path(route='update_property/<str:pk>/', view=views.update_property, name="update_property"),
    path(route='view_property/<str:pk>/', view=views.view_property, name="view_property"),

    path(route='view_all_properties', view=views.view_all_properties, name="view_all_properties"),
    path(route='property_admin', view=views.display_property_admin, name="property_admin"),

    path(route='add_property', view=views.add_property, name="add_property"),
    path(route='add_user', view=views.add_user, name="add_user"),

    path(route='agent_dash', view=views.agent_properties, name="agent_dash"),
    #path(route='dashboard', view=views.dashboard, name="dashboard"),
    
	path(route='make_rent_transaction', view=views.make_rent_transaction, name="make_rent_transaction"),
    path(route='make_buy_sell_transaction', view=views.make_buy_sell_transaction, name='make_buy_sell_transaction'),

    path(route='view__buySell_transactions', view=views.view__buySell_transactions, name='view__buySell_transactions'),
    path(route='view_rent_transactions', view=views.view_rent_transactions, name='view_rent_transactions')
]