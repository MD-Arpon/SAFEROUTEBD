from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import IncidentForm, StreetLightForm, CrowdReportForm
from .models import Incident

@login_required
def report_incident(request):
    if request.method == 'POST':
        form = IncidentForm(request.POST, request.FILES)
        if form.is_valid():
            incident = form.save(commit=False)
            incident.user = request.user
            incident.save()
            messages.success(request, "Incident reported successfully!")
            return redirect('reports:incident_list')
    else:
        form = IncidentForm()
    return render(request, 'reports/report_incident.html', {'form': form})

@login_required
def report_light(request):
    if request.method == 'POST':
        form = StreetLightForm(request.POST)
        if form.is_valid():
            light = form.save(commit=False)
            light.user = request.user
            light.save()
            messages.success(request, "Streetlight status reported!")
            return redirect('reports:incident_list')
    else:
        form = StreetLightForm()
    return render(request, 'reports/report_light.html', {'form': form})

@login_required
def report_crowd(request):
    if request.method == 'POST':
        form = CrowdReportForm(request.POST)
        if form.is_valid():
            crowd = form.save(commit=False)
            crowd.user = request.user
            crowd.save()
            messages.success(request, "Crowd density reported!")
            return redirect('reports:incident_list')
    else:
        form = CrowdReportForm()
    return render(request, 'reports/report_crowd.html', {'form': form})

def incident_list(request):
    incidents = Incident.objects.all().order_by('-created_at')
    return render(request, 'reports/incident_list.html', {'incidents': incidents})