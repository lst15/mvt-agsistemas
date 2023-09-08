from django import forms

from control.models import ControlModel
from vehicles.models import VehicleModel
from drivers.models import DriverModel
import datetime 
class ControlForm(forms.ModelForm):

  departure_time = forms.TimeField(
    initial=datetime.date.today,
    label="Hora saida",
    widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control transaction'}, format='%H:%M'),
    input_formats=('%H:%M',)
  )
  
  vehicle = forms.ModelChoiceField(
      label="Veiculo",
      queryset=VehicleModel.objects.all(),  # Queryset com todos os veículos disponíveis
      empty_label="Selecione um veículo",  # Rótulo padrão para a opção vazia
      widget=forms.Select(attrs={'class': 'form-control transaction'}),  # Use um menu suspenso como widget
  )
  
  driver = forms.ModelChoiceField(
      label="Motorista",
      queryset=DriverModel.objects.all(),  # Queryset com todos os veículos disponíveis
      empty_label="Selecione um motorista",  # Rótulo padrão para a opção vazia
      widget=forms.Select(attrs={'class': 'form-control transaction'})  # Use um menu suspenso como widget
  )
  departure_date = forms.DateField(
    initial=datetime.date.today,
    label="Data saida",
    # widget=forms.DateInput(attrs={'class': 'form-control transaction'})
    widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control transaction'}, format='%Y-%m-%d'),
    input_formats=('%Y-%m-%d',)
    )
  
  #departure_time = forms.CharField(label="Hora saida", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
  departure_km = forms.CharField(label="KM Saida", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
  departure_destination = forms.CharField(label="Saida destino", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
  
  return_date = forms.DateField(
    initial=datetime.date.today,
    label="Data retorno",
    # widget=forms.DateInput(attrs={'class': 'form-control transaction'})
    widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control transaction'}, format='%Y-%m-%d'),
    input_formats=('%Y-%m-%d',)
    )
  
  return_time = forms.TimeField(
    initial=datetime.date.today,
    label="Hora retorno",
    widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control transaction'}, format='%H:%M'),
    input_formats=('%H:%M',)
  )
  
  return_km = forms.CharField(label="KM Retorno", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))

  class Meta:
    model = ControlModel
    fields = [
      'vehicle',
      'driver',
      'departure_date',
      'departure_time',
      'departure_km',
      'departure_destination',
      'return_date',
      'return_time',
      'return_km',
    ]  