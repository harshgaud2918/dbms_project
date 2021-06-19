from django.urls import path
from . import views

urlpatterns = [
    path(route='', view=views.index, name="home"),
	
    path('logout', views.logoutUser, name="logout"),
    path('logout_admin', views.logoutUser_admin, name="logout_admin"),
    
	path(route='login_admin', view=views.login_admin, name="login_admin"),
    path(route='login_agent', view=views.login_agent, name="login_agent"),

    path(route='agent_properties', view=views.agent_properties, name="agent_properties"),
    
    path(route='update_property/<str:pk>/', view=views.update_property, name="update_property"),
    path(route='view_property/<str:pk>/', view=views.view_property, name="view_property"),

    path(route='view_all_properties', view=views.view_all_properties, name="view_all_properties"),    

    path(route='add_property', view=views.add_property, name="add_property"),
    path(route='add_user', view=views.add_user, name="add_user"),

    path(route='agent_dash', view=views.agent_dash, name="agent_dash"),
    path(route='admin_dash', view=views.admin_dash, name='admin_dash'),
    
    
	path(route='make_rent_transaction', view=views.make_rent_transaction, name="make_rent_transaction"),
    path(route='make_buy_sell_transaction', view=views.make_buy_sell_transaction, name='make_buy_sell_transaction'),

    path(route='view__buySell_transactions', view=views.view__buySell_transactions, name='view__buySell_transactions'),
    path(route='view_rent_transactions', view=views.view_rent_transactions, name='view_rent_transactions'),

    path(route='view_all_agents', view=views.view_all_agents, name='view_all_agents'),

    path(route='view_agent_sales_report/<str:pk>/', view=views.view_agent_sales_report, name='view_agent_sales_report'),
    path(route='list_properties', view=views.list_properties, name='list_properties'),

    
]