from django.shortcuts import render, redirect
from .models import Registros
from .forms import MyAuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate  #login para generar sessionid/cookie
from django.contrib.auth.models import User 
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required # decorador para proteger rutas


# Create your views here.
def home(request):
    return render(request, 'home.html', {"name": request.user })


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    username=request.POST["username"], password=request.POST["password1"], first_name=request.POST["name"], email= request.POST["email"])
                user.save()
                login(request, user) #generar cookie
                return redirect('home')
            except IntegrityError: #comprobar integridad en la db
                return render(request, 'signup.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'signup.html', {"form": UserCreationForm, "error": "Passwords did not match."})


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": MyAuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": MyAuthenticationForm, "error": "Username or password is incorrect."})
        #Guardar sessionid/cookie
        login(request, user)
        return redirect('home')


#Eliminar la cookie
@login_required
def signout(request):
    logout(request)
    return redirect('home')


@login_required
def matriculas(request): 
  registros = Registros.objects.filter(user=request.user)
  return render(request, 'index.html', {"registros": registros})

@login_required
def generar_matricula(request):  
  try:
    programa = request.POST['programa']  
    materia = request.POST['materia']
    creditos = request.POST['creditos']
    user = request.user
    registro = Registros.objects.create(
      programa=programa,
      materia=materia,
      creditos=creditos,
      user=user)

    return redirect('matriculas')
  except ValueError:
     registros = Registros.objects.filter(user=request.user)
     return render(request, 'index.html', {"registros": registros, "error": "Error generando la matricula"})

@login_required
def borrar (request, id):
  registro = Registros.objects.get(id = id)  
  registro.delete()
  return redirect('matriculas')

@login_required
def editar (request, id):
  registro = Registros.objects.get(id = id)
  print(id) 
  print(registro) 
  print(registro)
  print(request) 
  return render(request, 'editar.html', {"registro": registro})

def actualizar (request, id):
  programa = request.POST['programa']
  materia = request.POST['materia']
  creditos = request.POST['creditos']

  registro = Registros.objects.get(id = id)
  registro.programa = programa
  registro.materia = materia
  registro.creditos = creditos

  registro.save()
  return redirect('matriculas')
