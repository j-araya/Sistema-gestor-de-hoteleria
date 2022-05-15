from django.forms import ModelForm

from . import models

class ClienteForm(ModelForm):

    class Meta:

        model = models.Cliente
        exclude = ['usuario']


