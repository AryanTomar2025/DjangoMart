from django import forms
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm,UsernameField,PasswordChangeForm,SetPasswordForm,PasswordResetForm
from django.contrib.auth.models import User
from . models import Customer

class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'autofocus': 'True',
               'class': 'form-control form-control-lg',  
                'placeholder': 'Enter your username',  
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter your email',
            }
        )
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter your password',
            }
        )
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Confirm your password',
            }
        )
    )
    class Meta:
        model= User
        fields = ['username','email','password1','password2']





class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
    password = forms.CharField(
        label='Password',  # Change `password1` to `password`
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your password',
            }
        )
    )



class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'locality', 'city', 'mobile', 'zipcode')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'locality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your locality'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your city'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your mobile number'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your zipcode'}),
        }




class  MyPasswordChangeForm(PasswordChangeForm):
    old_password=forms.CharField(label='Old Password',widget=forms.PasswordInput(
        attrs={'autofocus':'True' ,'autocomplete':'current-password','class':'form-control'}
    ))
    new_password1=forms.CharField(label='New Password',widget=forms.PasswordInput(
        attrs={'autofocus':'True' ,'autocomplete':'current-password','class':'form-control'}
    ))
    new_password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(
        attrs={'autofocus':'True' ,'autocomplete':'current-password','class':'form-control'}
    ))


class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))


class MySetPasswordForm(SetPasswordForm):
    new_password1=forms.CharField(label='New Password',widget=forms.PasswordInput(
        attrs={'autofocus':'True' ,'autocomplete':'current-password','class':'form-control'}
    ))
    new_password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(
        attrs={'autofocus':'True' ,'autocomplete':'current-password','class':'form-control'}
    ))