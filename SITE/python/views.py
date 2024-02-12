from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accueil')
        else:
            # Gérer le cas d'authentification invalide
            return render(request, 'login_other.html', {'error': 'Nom d\'utilisateur ou mot de passe incorrect'})
    else:
        return render(request, 'login_other.html')
