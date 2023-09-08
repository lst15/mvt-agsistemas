# -*- encoding: utf-8 -*-
"""

"""

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse, QueryDict
from django import template
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import View
from django.contrib import messages

from vehicles.forms import VehicleForm
from vehicles.models import VehicleModel
from vehicles.utils import set_pagination

class CreateX(View):
    context = {'segment': 'vehiclecreate'}

    def post(self, request):        
        form = VehicleForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Veiculo criado com sucesso")
            return redirect('vehicleitens')

        if form.errors:
            print(form.errors)
            messages.error(request, "Preencha os campos")
            return redirect('vehicleitens')

    def get(self, request):
        # Renderize o formulário HTML usando o template e o formulário DriverForm
        form = VehicleForm()
        self.context['form'] = form

        html_template = loader.get_template('app/vehicleitens/register.html')
        return HttpResponse(html_template.render(self.context, request))

class VehicleView(View):
    context = {'segment': 'vehicleitens'}

    def get(self, request, pk=None, action=None):

        if pk and action == 'edit':
            context, template = self.edit(request, pk)
        else:
            context, template = self.list(request)

        if not context:
            html_template = loader.get_template('page-500.html')
            return HttpResponse(html_template.render(self.context, request))

        return render(request, template, context)

    def post(self, request, pk=None, action=None):
        self.update_instance(request, pk)
        return redirect('vehicleitens')

    def delete(self, request, pk, action=None):
        vehicleiten = self.get_object(pk)
        vehicleiten.delete()

        redirect_url = None
        if action == 'single':
            messages.success(request, 'Item deletado com sucesso')
            redirect_url = reverse('vehicleitens')

        response = {'valid': 'success', 'message': 'Item deletedo com sucesso', 'redirect_url': redirect_url}
        return JsonResponse(response)

    """ Get pages """

    def list(self, request):
        filter_params = None

        search = request.GET.get('search')
        if search:
            filter_params = None
            for key in search.split():                
                if key.strip():
                    if not filter_params:
                        filter_params = Q(vehicle_plate__icontains=key.strip())
                    else:
                        filter_params |= Q(vehicle_plate__icontains=key.strip())

        vehicleitens = VehicleModel.objects.filter(filter_params) if filter_params else VehicleModel.objects.all().order_by("vehicle_plate")

        self.context['vehicleitens'], self.context['info'] = set_pagination(request, vehicleitens)
        if not self.context['vehicleitens']:
            return False, self.context['info']

        return self.context, 'app/vehicleitens/list.html'

    def edit(self, request, pk):
        vehicleiten = self.get_object(pk)

        self.context['vehicleiten'] = vehicleiten
        self.context['form'] = VehicleForm(instance=vehicleiten)

        return self.context, 'app/vehicleitens/edit.html'


    """ Common methods """

    def get_object(self, pk):
        vehicleiten = get_object_or_404(VehicleModel, id=pk)
        return vehicleiten

    def update_instance(self, request, pk, is_urlencode=False):
        vehicleiten = self.get_object(pk)
        form_data = QueryDict(request.body) if is_urlencode else request.POST
        form = VehicleForm(form_data, instance=vehicleiten)
        if form.is_valid():
            form.save()
            if not is_urlencode:
                messages.success(request, 'Item salvo com sucesso')

            return True, 'Item salvo com sucesso'

        if not is_urlencode:
            messages.warning(request, 'Ocorreu um erro, tente novamente mais tarde')
        return False, 'Error Occurred. Please try again.'
