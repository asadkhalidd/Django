from django.shortcuts import render, redirect
# Create your views here.
from .forms import UserForm
from .models import User



def user_list(request):
	context = {"user_list": User.objects.all()}
	return render(request, 'accounts/user_list.html', context)
	
def user_form(request, id=0):
	if request.method == "GET":
		if id == 0:
			form = UserForm()
		else:
			user = User.objects.get(pk=id)
			form = UserForm(instance=user)
		return render(request, "accounts/user_form.html", {"form": form})
	else:
		if id == 0:
			form = UserForm(request.POST)
		else:
			user = User.objects.get(pk=id)
			form = UserForm(request.POST, instance=user)
		if form.is_valid():
			form.save()
		return redirect("/user_list")

def user_delete(request,id):
    user = User.objects.get(pk=id)
    user.delete()
    return redirect("/user_list")





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

def virtualreality(request):
	return render(request, 'accounts/virtual-reality.html')






