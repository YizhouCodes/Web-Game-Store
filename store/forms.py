from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import GeneralUser

class signUpFormPlayer(UserCreationForm):

	class Meta:
		model = GeneralUser
		date_of_birth = forms.DateTimeField(initial="", input_formats=['%d/%m/%Y %H:%M'])

		widgets = {
            'date_of_birth': forms.DateInput(attrs={"placeholder":"Date of birth", 'class':'datepicker'}),
			'email': forms.EmailInput(attrs={"placeholder": "Email","class": "form-control"}),
			'username': forms.TextInput(attrs={"placeholder": "Username","class": "form-control"}),
			'password1': forms.TextInput(attrs={"placeholder": "Password","class": "form-control"}),
			'password2': forms.PasswordInput(attrs={"placeholder": "Confirm Password","class": "form-control"}),

        }

		fields = ('username', 'email', 'date_of_birth', 'password1', 'password2')

class signUpFormDeveloper(UserCreationForm):

	class Meta:
		model = GeneralUser
		widgets = {
	            'payment_info': forms.TextInput(attrs={"placeholder":"Payment info","class": "form-control"}),
				'email': forms.EmailInput(attrs={"placeholder": "Email","class": "form-control"}),
				'username': forms.TextInput(attrs={"placeholder": "Username","class": "form-control"}),
				'password1': forms.PasswordInput(attrs={"placeholder": "Password","class": "form-control"}),
				'password2': forms.PasswordInput(attrs={"placeholder": "Confirm Password","class": "form-control"}),

	        }
		fields = ('username', 'email', 'payment_info', 'password1', 'password2')
