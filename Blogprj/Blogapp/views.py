from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Task
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    paginate_by = 5
    context_object_name = 'task'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Context to count incomplete tasks
        #context['count'] = context['task'].filter(complete=False).count()

        search_input = self.request.GET.get('search_area') or ''  # Updated search parameter name
        if search_input:
            context['task'] = context['task'].filter(title__icontains=search_input)
            context['search_input'] = search_input
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    paginate_by = 4  # Number of items per page
    context_object_name = 'task'
   
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('task')

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('task')

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task')

class CustomLoginView(LoginView):
    template_name = 'Blogapp/login.html'
    redirect_authenticated_user = False

    def get_success_url(self):
        return reverse_lazy('task')
    
class CustomLogoutView(LogoutView):
    template_name = 'Blogapp/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('login')
    
class RegisterPage(FormView):
    template_name = 'Blogapp/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('task')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('task')
        return super(RegisterPage, self).get(*args, **kwargs)
