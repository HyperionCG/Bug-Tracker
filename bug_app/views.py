from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from bug_app.models import Ticket, MyUser
from bug_app.forms import TicketForm, LoginForm, SignUpForm, EditTicketForm
from bug_project import settings

# Create your views here.

def index(request):
    new_tickets = Ticket.objects.filter(status="New")
    tickets_in_progress =  Ticket.objects.filter(status="In Progress")
    invalid_tickets =  Ticket.objects.filter(status="Invalid")
    done_tickets =  Ticket.objects.filter(status="Done")
    return render(
        request, 'index.htm',
         {
             'new_tickets': new_tickets, 
             'tickets_in_progress': tickets_in_progress, 
             'invalid_tickets': invalid_tickets, 
             'done_tickets': done_tickets
             })

def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    form = LoginForm()
    return render(request, 'generic_form.htm', {'form':form})

def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))

@login_required
def ticket_edit(request, id):
    file = Ticket.objects.get(id=id)
    if request.method == "POST":
        form = EditTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            file.title = data['title']
            file.description = data['description']
            file.status = data['status']
            file.assigned = data['assigned']
            file.completed = data['completed']
            file.save()
            return HttpResponseRedirect(reverse('ticket_detail', args=(id,)))

    form = EditTicketForm(initial={
            'title': file.title,
            'description': file.description,
    })
    return render(request, "generic_form.htm", {'form': form})

def signupview(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = MyUser.objects.create_user(
                username=data['username'],
                password=data['password'],
                )
            return HttpResponseRedirect(reverse('homepage'))
    
    form = SignUpForm()
    return render(request, 'generic_form.htm', {'form':form})

@login_required
def add_ticket(request):
    html = "generic_form.htm"
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Ticket.objects.create(
                title=data['title'],
                description=data['description'],
                filer = request.user
            )
            return HttpResponseRedirect(reverse('homepage'))
    
    form = TicketForm()
    return render(request, html, {"form": form})

def user_view(request, id):
    user = MyUser.objects.get(id=id)
    filed = Ticket.objects.filter(filer=user)
    assigned_user = Ticket.objects.filter(assigned=user)
    completed_user = Ticket.objects.filter(completed=user)
    return render(request,'userpage.htm', 
    {'user': user, 
     'filed': filed, 
     'assigned_user': assigned_user, 
     'completed_user': completed_user })


def ticket_detail_view(request, id):
    ticket = Ticket.objects.get(id=id)
    return render(request, 'ticket_detail.htm', {'ticket': ticket})
@login_required
def assigning_ticket_view(request, id):
    ticket = Ticket.objects.get(id=id)
    ticket.status = 'In Progress'
    ticket.assigned = request.user
    ticket.completed = None
    ticket.save()
    return HttpResponseRedirect(reverse('ticket_detail.htm', args=(id,)))

@login_required
def completed_ticket_view(request, id):
    ticket = Ticket.objects.get(id=id)
    ticket.status = 'Done'
    ticket.assigned = None
    ticket.completed = request.user
    ticket.save()
    return HttpResponseRedirect(reverse('ticket_detail.htm', args=(id,)))

@login_required
def invalid_ticket_view(request, id):
    ticket = Ticket.objects.get(id=id)
    ticket.status = 'Invalid'
    ticket.assigned = None
    ticket.completed = None
    ticket.save()
    return HttpResponseRedirect(reverse('ticket_detail.htm', args=(id,)))