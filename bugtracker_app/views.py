from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from bugtracker_app.models import CustomUser, BugTicket
from bugtracker_app.forms import LogInForm, AddUserForm, BugTicketForm

# Create your views here.
@login_required
def index(request):
    data = BugTicket.objects.all()
    return render(request, 'index.htm', {'data': data})

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


@login_required
def addbug(request):
    html = 'generic_form.htm'

    if request.method == 'POST':
        form = BugTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            bug = BugTicket.objects.create(
                title=data['title'],
                description=data['description'],
                filed_by=request.user,
            )
            return HttpResponseRedirect(reverse('home'))

    form = BugTicketForm()
    return render(request, html, {'form': form})


def bug_edit(request, id):
    bug = BugTicket.objects.get(id=id)
    if request.method == 'POST':
        form = BugTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            bug.title = data['title']
            bug.description = data['description']
            bug.ticket_status = data['ticket_status']
            bug.save()
            return HttpResponseRedirect()

    form = BugTicketForm(initial={
        'title': bug.title,
        'description': bug.description
    })
    return render(request, 'generic_form.htm', {'form': form})


def bugs(request, id):
    data = BugTicket.objects.get(id=id)
    return render(request, 'bugs.htm', {'data': data})


def user_info(request, id):
    person = CustomUser.objects.get(id=id)
    assigned = BugTicket.objects.filter(assigned_user=person)
    filed = BugTicket.objects.filter(filed_by=person)
    completed = BugTicket.objects.filter(completed_by=person)
    return render(request, 'user.htm', 
                    {'user': person, 'assigned': assigned,
                    'filed': filed, 'completed': completed})
