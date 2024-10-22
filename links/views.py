from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
# Create your views here.
@login_required
def home(request):
    return render(request, 'links/index.html')
@login_required
def mentalhealth(request):
    return render(request, 'links/mental_health.html')
@login_required
def economic(request):
    return render(request, 'links/economic.html')
@login_required
def team(request):
    return render(request, 'links/team.html')