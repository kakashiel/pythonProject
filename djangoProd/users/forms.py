from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.validators import RegexValidator
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed. (ex France: +33")
    # validators should be a list
    phone = forms.CharField(validators=[
                            phone_regex], max_length=17, help_text='Required', label='Phone number')
    reasonOnTheSite = forms.CharField(max_length=2000,
                                      widget=forms.Textarea(),
                                      label='Why do you need Rgpd search engine?')
    email = forms.EmailField(help_text='Required')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'password1',
                  'password2', 'phone', 'reasonOnTheSite')
    

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields