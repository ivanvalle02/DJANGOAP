from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


#View for Login
def login_views(request):
    template_name = "auth-login.html" 
      
    # Verifica si el usuario ya está autenticado
    if request.user.is_authenticated and request.user.is_active:
        return redirect('home')
   
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if request.user.is_active:
                  login(request, user)
            return redirect('home') 
    else:
          
            messages.error(request, 'Invalid login credentials or User is not active')
    return render(request,template_name)

# View for Register
def register_view(request):
    template_name = "auth-register.html"
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        # Validar que las contraseñas coincidan
        if password != password_confirmation:
            messages.error(request, "Las contraseñas no coinciden.")
            return render(request, template_name)

        # Validar si el nombre de usuario ya existe
        if User.objects.filter(username=username).exists():
            messages.error(request, "Este nombre de usuario ya está en uso.")
            return render(request, template_name)
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "El correo ya existe")
            return render(request, template_name)
      
            user = User(
                username=username,
                email=email,
                password=make_password(password), 
                is_active = 0
            )
            user.save()
            messages.success(request, "Usuario registrado exitosamente.") 
    return render(request,template_name)

# View for Forgot the Password
def forgot_view(request):
    template_name = "auth-forgot-password.html"
    return render(request,template_name)


# View for login 
def logout_view(request):
    logout(request)
    return redirect('login')