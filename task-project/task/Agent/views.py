from django.shortcuts import render
from .models import Agent

def display(request):
    lists = Agent.objects.all()
    return render(request, 'Agent/details.html', {'lists': lists})
    
def map(request, lat, long):
    return render(request, 'Agent/map.html',{'lat':lat,'long':long})