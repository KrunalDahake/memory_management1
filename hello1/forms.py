from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django import forms
# from django.contrib.auth.models import User
from .models import User,Product
from django.utils.translation import gettext_lazy as _

# This class is for signnup form which is provide by django and we have to customize it for better design

class SignUpForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Password Confirm',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['first_name','last_name','email','mobile','address']   # Change the username field as email field
        labels={'email':'Email'}
        widgets={'email':forms.EmailInput(attrs={'class':'form-control'}),
                 'first_name':forms.TextInput(attrs={'class':'form-control'}),
                 'last_name':forms.TextInput(attrs={'class':'form-control'}),
                 'mobile':forms.TextInput(attrs={'class':'form-control'}),
                 'address':forms.TextInput(attrs={'class':'form-control'}),
                 }
        

# This class is for login form which is provide by django and we have to customize it for better design        
class LoginForm(AuthenticationForm):
    # email=UsernameField(widget=forms.EmailInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(label=_('Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'})) 
    class Meta:
        model=User 
        fields=['email']
        labels={'email':'Email'}
        widgets={'email':forms.EmailInput(attrs={'class':'form-control'}),
                 
        }


# This class is a bookentry form for our staff user,they can fill all the information about book
# we have to customize it for applying external classes
class Bookentry(forms.ModelForm):
    class Meta:
        model = Product
        fields=('name','auth_name','price','description','image')
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),
                'auth_name':forms.TextInput(attrs={'class':'form-control'}),
                'price':forms.NumberInput(attrs={'class':'form-control'}),
                'description':forms.TextInput(attrs={'class':'form-control'}),
                'image':forms. ClearableFileInput(attrs={'class':'form-control'}),
                }