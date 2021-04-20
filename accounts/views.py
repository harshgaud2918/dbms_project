from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.core.management.commands import makemessages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .filters import *

# Create your views here.
def login_as(request):
    return render(request, 'login_as.html')

def register(request):
    return render(request, 'register.html')

def login_admin(request):
    return render(request, 'login_admin.html')

def login_agent(request):
    agents = Agent.objects.all()    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if ((Agent.objects.filter(username=username))):
            curr_agent = Agent.objects.get(username=username)
            currentLogin = Login.objects.get(username=username)
            if currentLogin.password == password:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)                                
                    return redirect ('agent_dash')                 
                            
            else:
                messages.warning(request, 'Incorrect Password !')
        else:
            messages.warning(request, 'Incorrect Username !')
    context = {'agents':agents}
    return render(request, 'login_agent.html',context)

# properties = [
#     {
#         'property_id' : 'abc',
#         'Type' : 'abc',
#         'Size' : 'abc',
#         'no_of_bedrooms' : 'abc',
#         'Address' : 'abc',
#         'Amount' : 'abc',
#         'Status' : 'abc',
#         'agent_id' : 'abc'
#     }
# ]

# agent_properties = [
#     {
#         'property_id' : 'abc',
#         'Type' : 'abc',
#         'Size' : 'abc',
#         'no_of_bedrooms' : 'abc',
#         'Address' : 'abc',
#         'Amount' : 'abc',
#         'Status' : 'abc'
#     }
# ]

def agent_properties(request):
    username = str(request.user)
    agent = Agent.objects.get(username=username)
    aid = agent.agent_id
    properties = Property.objects.filter(agent=aid)    
    agentfilter=PropertyFilter(request.GET,queryset=properties)
    properties=agentfilter.qs
    
    context = {'agent':agent,'properties':properties,'agentfilter':agentfilter}
    return render(request, 'agent_properties.html', context)

def view_all_properties(request):
    username = str(request.user)
    agent = Agent.objects.get(username=username)
    aid = agent.agent_id
    properties = Property.objects.all()    
    agentfilter=PropertyFilter(request.GET,queryset=properties)
    properties=agentfilter.qs
    
    context = {'agent':agent,'properties':properties,'agentfilter':agentfilter}
    return render(request, 'view_all_properties.html', context)

def display_property_agent(request):
    context={}
    return render(request, 'property_agent.html', context)

def display_property_admin(request):
    context={}
    return render(request, 'property_admin.html', context)

def add_property(request):
    username = str(request.user)
    agent = Agent.objects.get(username=username)
    aid = agent.agent_id
    form = AddPropertyForm()
    if request.method == 'POST':
        form = AddPropertyForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            if obj.has_changed():
                obj.agent = aid
            return redirect('agent_dash')

    context = {'agent':agent,'form':form}    
    return render(request, 'agent_add_prop.html',context)

def update_property(request,pk):
    username = str(request.user)
    agent = Agent.objects.get(username=username)
    aid = agent.agent_id
    prop = Property.objects.get(property_id=pk) 
    form = AddPropertyForm(instance=prop)
    if request.method == 'POST':
        form = AddPropertyForm(request.POST,instance=prop)
        if form.is_valid():
            obj = form.save(commit=False)
            
            obj.save()
            return redirect('agent_dash')

    context = {'agent':agent,'form':form}    
    return render(request, 'agent_add_prop.html',context)

def view_property(request,pk):
    username = str(request.user)
    agent = Agent.objects.get(username=username)
    aid = agent.agent_id
    prop = Property.objects.get(property_id=pk) 
    context = {'agent':agent,'property':prop}    
    return render(request, 'view_property_details.html',context)

def add_user(request):
    
    return render(request, 'agent_add_user.html')

# def agent_dash(request):
#     storage = messages.get_messages(request)
#     agentInfo=list()
#     for message in storage:
#         username = message
#     print(username)
#     agent = Agent.objects.get(username=username)
#     context = {'agent': agent}
#     messages.success(request,username)
#     return render(request, 'agent_dash.html',context)
def agent_dash(request):
    username = str(request.user)
    agent = Agent.objects.get(username=username)

    context = {'agent':agent}
    return render(request, 'agent_dash.html',context)

def logoutUser(request):
	logout(request)
	return redirect('home')

def index(request):
    return render(request, 'login_as.html')

def make_rent_transaction(request):
    return render(request, 'make_rent_transaction.html')

def make_buy_sell_transaction(request):
    return render(request, 'make_buy_sell_transaction.html')


def view_transactions(request):
    username = str(request.user)
    agent = Agent.objects.get(username=username)
    aid = agent.agent_id
    buy_sell_transactions = BuySellTransaction.objects.filter(agent=aid) 
    rent_transactions = RentTransaction.objects.filter(agent=aid)   
        
    context = {'agent':agent,'buy_sell_transactions':buy_sell_transactions,'rent_transactions':rent_transactions}
    return render(request, 'view_transactions.html',context)