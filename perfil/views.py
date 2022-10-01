from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse


class Criar(ListView):
    pass


# host/perfil/update
class Update(View):
    pass


# host/perfil/login
class Login(View):
    pass

# host/perfil/logout
class Logout(View):
    pass
