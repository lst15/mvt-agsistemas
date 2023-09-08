from django import forms

from control.models import ControlModel
from vehicles.models import VehicleModel
from drivers.models import DriverModel

class ControlForm(forms.ModelForm):
  vehicle = forms.ModelChoiceField(
      label="Veiculo",
      queryset=VehicleModel.objects.all(),  # Queryset com todos os veículos disponíveis
      empty_label="Selecione um veículo",  # Rótulo padrão para a opção vazia
      widget=forms.Select(attrs={'class': 'form-control transaction'}),  # Use um menu suspenso como widget
  )
  driver = forms.ModelChoiceField(
      label="Motorista",
      queryset=DriverModel.objects.all(),  # Queryset com todos os veículos disponíveis
      empty_label="Selecione um veículo",  # Rótulo padrão para a opção vazia
      widget=forms.Select(attrs={'class': 'form-control transaction'})  # Use um menu suspenso como widget
  )
  departure_date = forms.CharField(label="Data saida", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
  departure_time = forms.CharField(label="Hora saida", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
  departure_km = forms.CharField(label="KM Saida", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
  departure_destination = forms.CharField(label="Saida destino", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
  return_date = forms.CharField(label="Data retorno", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
  return_time = forms.CharField(label="Hora retorno", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
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