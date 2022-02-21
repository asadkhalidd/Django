from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import *

def dashboard(request):
	return render(request, 'accounts/dashboard.html')

def billing(request):
	return render(request, 'accounts/billing.html')

def notifications(request):
	return render(request, 'accounts/notifications.html')

def profile(request):
	return render(request, 'accounts/profile.html')

def rtl(request):
	return render(request, 'accounts/rtl.html')

def signin(request):
	return render(request, 'accounts/sign-in.html')

def signup(request):
	return render(request, 'accounts/sign-up.html')

def tables(request):
	return render(request, 'accounts/tables.html')

def virtualreality(request):
	return render(request, 'accounts/virtual-reality.html')