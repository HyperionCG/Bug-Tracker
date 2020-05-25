from django.shortcuts import render
from bug_app.models import Ticket

# Create your views here.
def index(request):
    data = Ticket.objects.all()
    return render(request, 'index.html', {'data': data})