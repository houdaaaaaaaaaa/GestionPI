from django.shortcuts import render

# Create your views here.
def tech(request):
    return render(request,'Ticket/index-tech.html')

def adm_tech(request):
    return render(request,'Ticket/index-adm.html')