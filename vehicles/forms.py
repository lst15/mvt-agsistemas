from django import forms

from vehicles.models import VehicleModel


class VehicleForm(forms.ModelForm):
    vehicle_plate = forms.CharField(label="Placa", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
    vehicle_brand = forms.CharField(label="Marca", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
    vehicle_model = forms.CharField(label="Modelo", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
    vehicle_oil_change_km = forms.CharField(label="Troca de óleo a cada KM", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))

    class Meta:
        model = VehicleModel
        fields =  ['vehicle_plate','vehicle_brand','vehicle_model','vehicle_oil_change_km']
