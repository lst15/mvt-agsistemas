from django import forms

from drivers.models import DriverModel


class DriverForm(forms.ModelForm):
    driver_name = forms.CharField(label="Nome completo", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
    driver_phone = forms.CharField(label="Telefone", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
    driver_license = forms.CharField(label="CNH", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))    

    class Meta:
        model = DriverModel
        fields =  ['driver_name','driver_phone','driver_license']