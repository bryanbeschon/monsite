from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user, get_user_model
from django.views.generic import CreateView
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from .forms import UsersRegisterForm
from .forms import UsersLoginForm
from .forms import UpdateForm

def login_view(request):
	form = UsersLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username = username, password = password)
		login(request, user)
		return redirect("/")
	return render(request, "siteweb/form.html", {
		"form" : form,
		"title" : "Se connecter",
	})

def register_view(request):
	form = UsersRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save()
		password = form.cleaned_data.get("password")	
		user.set_password(password)
		user.save()
		new_user = authenticate(username = user.username, password = password)
		login(request, new_user)
		return redirect("/siteweb/login")
	return render(request, "siteweb/form.html", {
		"title" : "S'inscrire",
		"form" : form,
	})

def logout_view(request):
	logout(request)
	return HttpResponseRedirect("/")

User = get_user_model()

def save_user_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            users =[get_user(request)];
            data['html_user_list'] = render_to_string('siteweb/templates/partial_user_list.html', {
                'users': users
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def user_update(request,pk):
	utilisateur = get_object_or_404(User, pk=pk)
	if request.method == 'POST':
		form = UpdateForm(request.POST, instance=utilisateur)
	else:
		form = UpdateForm(instance=utilisateur)
	return save_user_form(request, form, 'siteweb/templates/partial_user_update.html')
    #return render(request, form, 'siteweb/partial_user_update.html')

def user_list(request):
    users = [get_user(request)];
    return render(request, 'siteweb/templates/user_list.html',{'users':users})