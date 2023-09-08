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

from drivers.forms import DriverForm
from drivers.models import DriverModel
from drivers.utils import set_pagination

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.views import View
from .forms import DriverForm  # Importe o formulário DriverForm

class Create(View):
    context = {'segment': 'drivercreate'}

    def post(self, request):
        form = DriverForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Motorista criado com sucesso")
            return redirect('driveritens')

        if form.errors:
            messages.error(request, "Preencha os campos")
            return redirect('driveritens')

    def get(self, request):
        # Renderize o formulário HTML usando o template e o formulário DriverForm
        form = DriverForm()
        self.context['form'] = form

        html_template = loader.get_template('app/driveritens/register.html')
        return HttpResponse(html_template.render(self.context, request))


class DriverView(View):
    context = {'segment': 'driveritens'}

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
        return redirect('driveritens')

    def delete(self, request, pk, action=None):
        driveriten = self.get_object(pk)
        driveriten.delete()

        redirect_url = None
        if action == 'single':
            messages.success(request, 'Item deletedo com sucesso')
            redirect_url = reverse('driveritens')

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
                        filter_params = Q(driver_name__icontains=key.strip())
                    else:
                        filter_params |= Q(driver_name__icontains=key.strip())

        driveritens = DriverModel.objects.filter(filter_params) if filter_params else DriverModel.objects.all()

        self.context['driveritens'], self.context['info'] = set_pagination(request, driveritens)
        if not self.context['driveritens']:
            return False, self.context['info']

        return self.context, 'app/driveritens/list.html'

    def edit(self, request, pk):
        driveriten = self.get_object(pk)

        self.context['driveriten'] = driveriten
        self.context['form'] = DriverForm(instance=driveriten)

        return self.context, 'app/driveritens/edit.html'

    """ Common methods """

    def get_object(self, pk):
        driveriten = get_object_or_404(DriverModel, id=pk)
        return driveriten

    def update_instance(self, request, pk, is_urlencode=False):
        driveriten = self.get_object(pk)
        form_data = QueryDict(request.body) if is_urlencode else request.POST
        form = DriverForm(form_data, instance=driveriten)
        if form.is_valid():
            form.save()
            if not is_urlencode:
                messages.success(request, 'Item salvo com sucesso')

            return True, 'driveriten saved successfully'

        if not is_urlencode:
            messages.warning(request, 'Ocorreu um erro, tente novamente mais tarde!')
        return False, 'Error Occurred. Please try again.'
