from django.contrib.auth import login, logout
from django.contrib.auth.models import Permission, Group
from django.contrib.auth.views import LoginView
from django.contrib.contenttypes.models import ContentType
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, DetailView
from .save import *
from .forms import *





class Home(ListView):
    model = User
    template_name = 'base.html'
    context_object_name = 'user'


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'


def logout_user(request):
    logout(request)
    return redirect('home')


class Profile(DetailView):
    model = Document
    context_object_name = 'detail'
    template_name = 'UserDetail.html'


class File_download(DetailView):
    model = Document
    context_object_name = "zagruzka"
    template_name = 'index.html'


#
# def upload_file(request):
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form:
#             document = form.save(commit=False)
#             document.User = 'root'
#             document.save()
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = DocumentForm()
#     return render(request, 'index.html', {'form': form})


def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = DocumentForm()
    return render(request, 'index.html', {'form': form})


