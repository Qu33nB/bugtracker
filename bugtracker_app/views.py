from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from bugtracker_app.models import CustomUser
from bugtracker_app.forms import LogInForm, AddUserForm, BugTicketForm
from bugtracker_project import settings

# Create your views here.
@login_required
def index(request):
    info = settings.AUTH_USER_MODEL
    return render(request, 'index.htm', {'info': info})

def loginview(request):
    html = 'generic_form.htm'
    
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
                )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('home'))
                )
    form = LogInForm()
    return render(request, html, {'form': form})


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


@login_required
def adduser(request):
    html = 'generic_form.htm'

    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = CustomUser.objects.create_user(
                username=data['username'],
                password=data['password'],
                display_name=data['display_name'],
            )
            return HttpResponseRedirect(reverse('home'))

    form = AddUserForm()
    return render(request, html, {'form': form})