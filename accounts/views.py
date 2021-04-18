from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login_as.html')

def register(request):
    return render(request, 'register.html')

def login_admin(request):
    return render(request, 'login_admin.html')

def login_agent(request):
    return render(request, 'login_agent.html')

properties = [
    {
        'property_id' : 'abc',
        'Type' : 'abc',
        'Size' : 'abc',
        'no_of_bedrooms' : 'abc',
        'Address' : 'abc',
        'Amount' : 'abc',
        'Status' : 'abc',
        'agent_id' : 'abc'
    }
]

agent_properties = [
    {
        'property_id' : 'abc',
        'Type' : 'abc',
        'Size' : 'abc',
        'no_of_bedrooms' : 'abc',
        'Address' : 'abc',
        'Amount' : 'abc',
        'Status' : 'abc'
    }
]

def agent_properties(request):
    context = {
        'properties' : properties,
        'agent_properties' : agent_properties
    }
    return render(request, 'agent_properties.html', context)

def display_property_agent(request):
    context = {
        'property' : 'blah'
    }
    return render(request, 'property_agent.html', context)

def display_property_admin(request):
    context = {
        'property' : 'blah'
    }
    return render(request, 'property_admin.html', context)

def add_property(request):
    return render(request, 'agent_add_prop.html')

def add_user(request):
    return render(request, 'agent_add_user.html')

def agent_dash(request):
    return render(request, 'agent_dash.html')
def index(request):
    return render(request, 'dashboard.html')
