from django.forms import ModelForm, DateInput
from django.forms.widgets import SelectDateWidget

from . import models

class ClienteForm(ModelForm):

    class Meta:

        model = models.Cliente
        exclude = ['usuario']

class PeriodoForm(ModelForm):

    class Meta:

        model = models.Reservacion
        fields = ['fecha_entrada', 'fecha_salida']

        widgets = {
            'fecha_entrada': SelectDateWidget(),
            'fecha_salida': SelectDateWidget(),
        }

class ReservacionForm(ModelForm):

    class Meta:

        model = models.Reservacion
        fields = ['fecha_entrada', 'fecha_salida']

        widgets = {
            'fecha_entrada': SelectDateWidget(),
            'fecha_salida': SelectDateWidget(),
        }

            
        


