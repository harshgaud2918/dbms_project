from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.core.management.commands import makemessages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .filters import *
from django.contrib.auth.decorators import login_required
from django import forms
import datetime


# Create your views here.

def login_admin(request):      
    if request.method == 'POST':
        print(request.POST['username'],request.POST['password'])
        usernam = request.POST['username']
        passw= request.POST['password']        
        user = authenticate(request, username=usernam, password=passw)
        if user is not None  :            
            login(request, user)   
            if request.user.is_superuser:
                return redirect ('admin_dash')    
            else:
                messages.warning(request, 'You Are Not Authorized to Enter ! ')
                return redirect ('logout_admin')
        messages.warning(request, 'Incorrect Username or Password!')  

    context = {}    
    return render(request, 'login_admin.html',context)

def logoutUser_admin(request):
	logout(request)
	return redirect('login_admin')

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


@login_required(login_url='home')
def agent_properties(request):
    username = str(request.user)
    agent = Agent.objects.get(username=username)
    aid = agent.agent_id
    properties = Property.objects.filter(agent=aid)    
    agentfilter=PropertyFilter(request.GET,queryset=properties)
    properties=agentfilter.qs
    
    context = {'agent':agent,'properties':properties,'agentfilter':agentfilter}
    return render(request, 'agent_properties.html', context)

@login_required(login_url='home')
def view_all_properties(request):
    username = str(request.user)
    agent = Agent.objects.get(username=username)
    aid = agent.agent_id
    properties = Property.objects.all()    
    agentfilter=PropertyFilter(request.GET,queryset=properties)
    properties=agentfilter.qs
    
    context = {'agent':agent,'properties':properties,'agentfilter':agentfilter}
    return render(request, 'view_all_properties.html', context)



@login_required(login_url='home')
def add_property(request):
    username = str(request.user)
    agent = Agent.objects.get(username=username)
    aid = agent.agent_id
    form = AddPropertyForm()
    if request.method == 'POST':
        form = AddPropertyForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.agent = agent
            obj.save()
            return redirect('agent_dash')

    context = {'agent':agent,'form':form}    
    return render(request, 'agent_add_prop.html',context)

@login_required(login_url='home')
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

@login_required(login_url='home')
def view_property(request,pk):
    username = str(request.user)
    agent = Agent.objects.get(username=username)
    aid = agent.agent_id
    prop = Property.objects.get(property_id=pk) 
    context = {'agent':agent,'property':prop}    
    return render(request, 'view_property_details.html',context)

@login_required(login_url='home')
def add_user(request):
    username = str(request.user)
    agent = Agent.objects.get(username=username)
    aid = agent.agent_id
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agent_dash')

    context = {'agent':agent,'form':form}    
    return render(request, 'add_user.html',context)

@login_required(login_url='home')
def agent_dash(request):
    username = str(request.user)
    agent = Agent.objects.get(username=username)
    aid = agent.agent_id
    properties = Property.objects.filter(agent=aid) 

    for_sale= Property.objects.filter(agent=aid,status='for_sale')
    for_lease= Property.objects.filter(agent=aid,status='for_lease')
    on_lease= Property.objects.filter(agent=aid,status='On_Lease')
    sold= Property.objects.filter(agent=aid,status='Sold')
    for_sale_count=len(for_sale)
    for_lease_count=len(for_lease)
    on_lease_count=len(on_lease)
    sold_count=len(sold)
    count=for_sale_count+for_lease_count+on_lease_count+sold_count


    all_for_sale= Property.objects.filter(status='for_sale')
    all_for_lease= Property.objects.filter(status='for_lease')
    all_on_lease= Property.objects.filter(status='On_Lease')
    all_sold= Property.objects.filter(status='Sold')
    all_for_sale_count=len(all_for_sale)
    all_for_lease_count=len(all_for_lease)
    all_on_lease_count=len(all_on_lease)
    all_sold_count=len(all_sold)
    all_count=all_for_sale_count+all_for_lease_count+all_on_lease_count+all_sold_count


    buy_sell=BuySellTransaction.objects.filter(agent=agent)
    buy_sell_count=len(buy_sell)

    rent=RentTransaction.objects.filter(agent=agent)
    rent_count=len(rent)
    agentfilter=PropertyFilter(request.GET,queryset=properties)
    properties=agentfilter.qs
    
    context = {'agent':agent,'properties':properties,'agentfilter':agentfilter,'for_lease_count':for_lease_count,
    'for_sale_count':for_sale_count,'on_lease_count':on_lease_count,'sold_count':sold_count,'count':count,
    'rent_count':rent_count,'buy_sell_count':buy_sell_count, 'all_for_sale_count':all_for_sale_count,
    'all_for_lease_count':all_for_lease_count,'all_on_lease_count':all_on_lease_count,'all_sold_count':all_sold_count,'all_count':all_count}
    return render(request, 'agent_dash.html',context)

def logoutUser(request):
	logout(request)
	return redirect('home')

def index(request):
    return render(request, 'login_as.html')

@login_required(login_url='home')
def make_rent_transaction(request):
    username = str(request.user)
    agent = Agent.objects.get(username=username)
    aid = agent.agent_id
    form = RentTransactionForm()    
    form.fields['property'].queryset = Property.objects.filter(status='for_lease').filter(agent=aid)
    if request.method == 'POST':               
        Pid = request.POST['property']
        prop = Property.objects.get(property_id=Pid)
        form = RentTransactionForm(request.POST)   
        if form.is_valid():
            print(form.data)            
            obj =  form.save(commit=False)            
            obj.date = datetime.date.today()
            obj.agent = agent
            obj.owner = prop.owner
            obj.save()
            Property.objects.filter(property_id=Pid).update(status='On_Lease')
            print(form.data)     
            return redirect('agent_dash')

    context = {'agent':agent,'form':form} 
    return render(request, 'make_rent_transaction.html',context)


@login_required(login_url='home')
def make_buy_sell_transaction(request):
    username = str(request.user)
    agent = Agent.objects.get(username=username)
    aid = agent.agent_id
    form = BuySellTransactionForm()    
    form.fields['property'].queryset = Property.objects.filter(status='For_Sale').filter(agent=aid)
    if request.method == 'POST':               
        Pid = request.POST['property']
        buyer_id = request.POST['buyer']
        buyer = Buyer.objects.get(buyer_id=buyer_id)
        prop = Property.objects.get(property_id=Pid)
        form = BuySellTransactionForm(request.POST)        
        if form.is_valid():
            print(form.data)            
            obj =  form.save(commit=False)            
            obj.date = datetime.date.today()
            obj.agent = agent
            obj.owner = prop.owner
            obj.save()
            Property.objects.filter(property_id=Pid).update(status='Sold')
            new_owner = Owner(owner_id=buyer_id,user=buyer.user)
            new_owner.save()
            Property.objects.filter(property_id=Pid).update(owner=buyer_id)
            print(form.data)     
            return redirect('agent_dash')

    context = {'agent':agent,'form':form} 
    return render(request, 'make_buy_sell_transaction.html',context)


@login_required(login_url='home')
def view__buySell_transactions(request):
    username = str(request.user)
    agent = Agent.objects.get(username=username)
    aid = agent.agent_id
    buy_sell_transactions = BuySellTransaction.objects.filter(agent=aid)       

    bsellfilter=TransactionFilter(request.GET,queryset=buy_sell_transactions)
    buy_sell_transactions=bsellfilter.qs

          
    context = {'agent':agent,'buy_sell_transactions':buy_sell_transactions,'bsellfilter':bsellfilter}
    return render(request, 'view_buySell_transactions.html',context)

@login_required(login_url='home')
def view_rent_transactions(request):
    username = str(request.user)
    agent = Agent.objects.get(username=username)
    aid = agent.agent_id
    
    rent_transactions = RentTransaction.objects.filter(agent=aid)   
    rentfilter=RentFilter(request.GET,queryset=rent_transactions)
    rent_transactions=rentfilter.qs
        
    context = {'agent':agent,'rent_transactions':rent_transactions,'rentfilter':rentfilter}
    return render(request, 'view_rent_transactions.html',context)

@login_required(login_url='home')
def admin_dash(request):

    username = str(request.user)

    properties = Property.objects.all()  
    total_properties = properties.count() 

    forSale = properties.filter(status='For_Sale').count()
    forLease = properties.filter(status='for_lease').count()
    sold = properties.filter(status='Sold').count()
    onLease = properties.filter(status='on_lease').count()    

    agents = Agent.objects.all()  
    total_agents = agents.count()

    bs_trans = BuySellTransaction.objects.all()  
    total_bsTrans = bs_trans.count() 

    rent_trans = RentTransaction.objects.all()  
    total_rentTrans = rent_trans.count()

    owners = Owner.objects.all()  
    total_owner = owners.count()

    buyers = Buyer.objects.all()  
    total_buyer = buyers.count()

    tenants = Tenant.objects.all()  
    total_tenant = tenants.count()
    
    context = {'properties':properties,'total_properties':total_properties,'forSale':forSale,
    'forLease':forLease,'sold':sold,'onLease':onLease,'agents':agents,'total_agents':total_agents,
    'bs_trans':bs_trans,'total_bsTrans':total_bsTrans,'rent_trans':rent_trans,'total_rentTrans':total_rentTrans,
    'owners':owners,'total_owner':total_owner,'buyers':buyers,'total_buyer':total_buyer,'tenants':tenants,
    'total_tenant':total_tenant}

    return render(request, 'admin_dash.html',context)

@login_required(login_url='home')
def view_all_agents(request):    
    agents = Agent.objects.all()
    context = {'agents':agents}
    return render(request, 'view_all_agents.html',context)


@login_required(login_url='home')
def view_agent_sales_report(request,pk):    
    agent = Agent.objects.get(agent_id=pk)

    aid = agent.agent_id
    properties = Property.objects.filter(agent=aid) 

    for_sale= Property.objects.filter(agent=aid,status='for_sale')
    for_lease= Property.objects.filter(agent=aid,status='for_lease')
    on_lease= Property.objects.filter(agent=aid,status='On_Lease')
    sold= Property.objects.filter(agent=aid,status='Sold')
    for_sale_count=len(for_sale)
    for_lease_count=len(for_lease)
    on_lease_count=len(on_lease)
    sold_count=len(sold)
    count=for_sale_count+for_lease_count+on_lease_count+sold_count


    transaction1=BuySellTransaction.objects.filter(agent=agent)    

    transaction2=RentTransaction.objects.filter(agent=agent)
    

    
    context = {'agent':agent,'properties':properties,'for_lease_count':for_lease_count,
    'for_sale_count':for_sale_count,'on_lease_count':on_lease_count,'sold_count':sold_count,'count':count,
    'transaction1':transaction1,'transaction2':transaction2 }
    
    return render(request, 'view_agent_sales_report.html',context)

@login_required(login_url='home')
def list_properties(request):    
    properties = Property.objects.all()    
    agentfilter=PropertyFilter(request.GET,queryset=properties)
    properties=agentfilter.qs    
    context = {'properties':properties,'agentfilter':agentfilter}    
    return render(request, 'list_properties.html',context)