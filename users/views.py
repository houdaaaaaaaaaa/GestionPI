from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request,'users/index.html')
def nw_tick(request):
    return render(request,'users/forms-elements.html')

def profile(request):
    return render(request,'users/users-profile.html')
def ticket_env(request):
    return render(request,'users/viewticket.html')
def lgoin(request):
    return render(request,'users/pages-lgoin.html')
def lgout(request):
    return render(request,'users/transport.html')
def dashboard(request):
    return render(request,'users/dashboard.html') 


