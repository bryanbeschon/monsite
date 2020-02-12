# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, get_user_model
from django import forms

class UsersLoginForm(forms.Form):
	username = forms.CharField(label = "Nom d'utilisateur")
	password = forms.CharField(label = "Mot de passe", widget = forms.PasswordInput,)

	def __init__(self, *args, **kwargs):
		super(UsersLoginForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({
		    'class': 'form-control',
		    "name":"username"})
		self.fields['password'].widget.attrs.update({
		    'class': 'form-control',
		    "name":"password"})

	def clean(self, *args, **keyargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")

		if username and password:
			user = authenticate(username = username, password = password)
			if not user:
				raise forms.ValidationError("Cet utilisateur n'existe pas")
			if not user.check_password(password):
				raise forms.ValidationError("Mot de passe incorrect")

		return super(UsersLoginForm, self).clean(*args, **keyargs)


User = get_user_model()

class UsersRegisterForm(forms.ModelForm):
	class Meta:
		model = User
		fields = [
			'username',
            'last_name',
			'first_name',
            'password',
			'email',
		]

	username = forms.CharField(label = "Nom d'utilisateur", max_length=30)	
	first_name = forms.CharField(label = "Prénom", max_length=30)	
	last_name = forms.CharField(label = "Nom", max_length=30)
	password = forms.CharField(label = "Mot de passe", max_length=20, widget = forms.PasswordInput)
	email = forms.EmailField(label = "Email")

	def __init__(self, *args, **kwargs):
		super(UsersRegisterForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({
		    'class': 'form-control',
		    'name':'username'})
		self.fields['last_name'].widget.attrs.update({
		    'class': 'form-control',
		    'name':'last_name'})
		self.fields['first_name'].widget.attrs.update({
		    'class': 'form-control',
		    'name':'first_name'})
		self.fields['password'].widget.attrs.update({
		    'class': 'form-control',
		    'name':'password'})
		self.fields['email'].widget.attrs.update({
		    'class': 'form-control',
		    'name':'email'})


	def clean(self, *args, **keyargs):
		username = self.cleaned_data.get("username")
		nom = self.cleaned_data.get("last_name")
		prenom = self.cleaned_data.get("first_name")
		password = self.cleaned_data.get("password")
		email = self.cleaned_data.get("email")
		
		username_qs = User.objects.filter(username=username)
		if username_qs.exists():
			raise forms.ValidationError("Ce nom d'utilisateur est déjà utilisé")

		email_qs = User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError("Cet email est déjà utilisé")

		#if len(password) < 8:	
		#	raise forms.ValidationError("Le mot de passe doit être supérieur à 8 caractères")


		return super(UsersRegisterForm, self).clean(*args, **keyargs)


class UpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
			'email',
		]

