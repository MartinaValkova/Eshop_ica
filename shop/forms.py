from django import forms
from django.contrib.auth.models import User


#captcha
from captcha.fields import ReCaptchaField



# Code for register user
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm password', widget=forms.PasswordInput)
    check = forms.BooleanField(required = True)
    email = forms.CharField(label='Email', widget=forms.EmailInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name']

    captcha = ReCaptchaField()   

    def check_password(self):
            if self.cleaned_data['password'] != self.cleaned_data['password2']:
                raise forms.ValidationError('Password fields do not match')
            return self.cleaned_data['password2']
        
