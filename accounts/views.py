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