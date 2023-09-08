from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, QueryDict,HttpResponse
from django.urls import reverse
from django.views import View
from django.contrib import messages
from django.db.models import Q
from django.template.loader import render_to_string
from control.forms import ControlForm
from control.models import ControlModel
from control.utils import set_pagination
from vehicles.models import VehicleModel
from django.template import loader

class Create(View):
    context = {'segment': 'drivercreate'}

    def post(self, request):
        form = ControlForm(request.POST)

        if form.is_valid():
          
            vehicle_id = request.POST.get("vehicle")
            vehicle = VehicleModel.objects.get(id=vehicle_id)
                                       
            form.save()
            messages.success(request, "Motorista criado com sucesso")                        
            
            controls = ControlModel.objects.filter(vehicle=vehicle_id)
            km_total = sum(control.distance_traveled for control in controls)
            km_left = vehicle.vehicle_oil_change_km - km_total        
            
            if km_left <= 0:          
                messages.error(request, "Veiculo necessita de uma nova troca de óleo")            
            
            return redirect('controlitens')

        if form.errors:
            messages.error(request, "Preencha os campos")
            return redirect('controlitens')

    def get(self, request):
        # Renderize o formulário HTML usando o template e o formulário DriverForm
        form = ControlForm()
        self.context['form'] = form

        html_template = loader.get_template('app//controlitens/register.html')
        return HttpResponse(html_template.render(self.context, request))

class ControlView(View):
    context = {'segment': 'controlitens'}

    def get(self, request, pk=None, action=None):

        if pk and action == 'edit':
            return self.edit(request, pk)
        elif pk and action == 'view':
            return self.viewDetail(request,pk)        
        return self.list(request)

    def post(self, request, pk=None, action=None):
        vehicle_id = request.POST.get("vehicle")
        vehicle = get_object_or_404(VehicleModel, id=vehicle_id)
        
        controls = ControlModel.objects.filter(vehicle=vehicle_id)
        km_total = sum(control.distance_traveled for control in controls)
        km_left = vehicle.vehicle_oil_change_km - km_total        
        
        if km_left <= 0:          
            messages.error(request, "Veiculo necessita de uma nova troca de óleo")
        
        self.update_instance(request, pk)
        return redirect('controlitens')

    def delete(self, request, pk, action=None):
        controliten = get_object_or_404(ControlModel, id=pk)
        controliten.delete()

        redirect_url = None
        if action == 'single':
            messages.success(request, 'Item deletedo com sucesso')
            redirect_url = reverse('controlitens')

        response = {'valid': 'success', 'message': 'Item deleted successfully', 'redirect_url': redirect_url}
        return JsonResponse(response)

    def list(self, request):
        filter_params = None

        search = request.GET.get('search')
        if search:
            filter_params = None
            for key in search.split():                
                if key.strip():
                    if not filter_params:
                        filter_params = Q(departure_date__icontains=key.strip())
                    else:
                        filter_params |= Q(departure_date__icontains=key.strip())

        controlitens = ControlModel.objects.filter(filter_params) if filter_params else ControlModel.objects.all()

        self.context['controlitens'], self.context['info'] = set_pagination(request, controlitens)
        if not self.context['controlitens']:
            return render(request, 'page-500.html', self.context)

        return render(request, 'app/controlitens/list.html', self.context)

    def edit(self, request, pk):
        controliten = get_object_or_404(ControlModel, id=pk)

        self.context['controliten'] = controliten
        self.context['form'] = ControlForm(instance=controliten)

        return render(request, 'app/controlitens/edit.html', self.context)

    def viewDetail(self, request, pk):
        controliten = get_object_or_404(ControlModel, id=pk)

        self.context['controliten'] = controliten
        self.context['form'] = ControlForm(instance=controliten)

        return render(request, 'app/controlitens/view.html', self.context)

    def get_object(self, pk):
        return get_object_or_404(ControlModel, id=pk)


    def update_instance(self, request, pk, is_urlencode=False):
        controliten = self.get_object(pk)
        form_data = request.POST if not is_urlencode else QueryDict(request.body)
        form = ControlForm(form_data, instance=controliten)
        if form.is_valid():
            form.save()
            if not is_urlencode:
                messages.success(request, 'Item salvo com sucesso')
            return True, 'controliten saved successfully'

        if not is_urlencode:
            messages.warning(request, 'Ocorreu um erro, tente novamente mais tarde!')
        return False, 'Error Occurred. Please try again.'
