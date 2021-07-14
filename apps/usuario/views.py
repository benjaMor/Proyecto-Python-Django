from django.contrib.auth.models import User
from django.contrib.auth.forms  import UserCreationForm
from django.views.generic import CreateView


from apps.usuario.forms import RegistroForm

class RegistroUsuario(CreateView):
    model = User 
    template_name = "Usuario/registrar.html"
    form_class = RegistroForm


