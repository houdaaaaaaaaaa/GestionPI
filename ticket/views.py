from django.shortcuts import render

# Create your views here.
def tech(request):
    return render(request,'Ticket/index-tech.html')

def adm_tech(request):
    return render(request,'Ticket/index-adm.html')
def rehard(request):
    return render(request,'Ticket/rehard.html')
def logisoft(request):
    return render(request,'Ticket/logisoft.html')
def matehard(request):
    return render(request,'Ticket/matehard.html')
def tecketresul(request):
    return render(request,'Ticket/tecketresul.html')
def listtech(request):
    return render(request,'Ticket/listtech.html')
def resoudre(request):
    return render(request,'Ticket/resoudre.html')
def resl(request):
    return render(request,'Ticket/resolu.html')
def reseaux(request):
    return render(request,'Ticket/reseaux.html')
def logiciel(request):
    return render(request,'Ticket/logiciel.html')
def web (request):
    return render(request,'Ticket/web.html')