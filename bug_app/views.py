from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from bug_app.models import Ticket, MyUser
from bug_app.forms import TicketForm, LoginForm, SignUpForm

# Create your views here.
def index(request):
    data = Ticket.objects.all()
    return render(request, 'index.html', {'data': data})

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
    return render(request, 'userpage.html', {'form':form})

def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))

@login_required
def ticket_edit(request, id):
    file = Ticket.objects.get(id=id)
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            file.title = data['title']
            file.description = data['description']
            file.save()
            return HttpResponseRedirect(reverse('', args=(id)))

        form = TicketForm(initial={
            'title': file.title,
            'description': file.description
        })
        return render(request, "ticket_detail.html", {'form': form})

def signupview(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = MyUser.objects.create_user(
                username=data['username'],
                password=data['password'],
                display_name=data['display_name']
                )
            return HttpResponseRedirect(reverse('homepage'))
    
    form = SignUpForm()
    return render(request, 'userpage.html', {'form':form})