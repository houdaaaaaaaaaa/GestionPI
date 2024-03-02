from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TicketForm

@login_required
def creer_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        print(request.POST)  # Ajout pour vérifier les données soumises
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.utilisateur = request.user
            ticket.save()
            print("Ticket créé avec succès:", ticket)  # Ajout pour vérifier le succès de la création
            return redirect('creer_ticket')  # Rediriger vers une vue de confirmation ou autre
        else:
            print("Erreurs de validation du formulaire:", form.errors)  # Ajout pour vérifier les erreurs de validation
    else:
        form = TicketForm()
    return render(request, 'users/forms-elements.html', {'form': form})

def index (request):
    return render(request,'users/index.html')
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


