from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Employee, Department, Location
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator

# Create your views here.
def index(request):
    return render(request, 'emp_app/index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

class EmployeeListView(ListView):
    model = Employee
    template_name = 'emp_app/list.html'

@method_decorator(login_required, name='dispatch')
class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = Employee
    template_name = 'emp_app/details.html'

class EmployeeCreateView(CreateView):
    model = Employee
    fields = ('eid', 'ename', 'eemail', 'econtact', 'edept')
    template_name = 'emp_app/create.html'


class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = ('eid', 'ename', 'eemail', 'econtact', 'edept')
    template_name = 'emp_app/create.html'

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'emp_app/delete.html'
    success_url = reverse_lazy('emp_app:list')
