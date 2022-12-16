from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField

from djangoweb.apps.users.models import UserProfileModel, AboutData

User = get_user_model()


class SignInForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password',)

        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'u-border-2 u-border-grey-10 u-grey-10 u-input u-input-rectangle u-input-1'},),
        #     'password': forms.PasswordInput(attrs={'class': 'u-border-2 u-border-grey-10 u-grey-10 u-input u-input-rectangle u-input-2'},),
        # }


class ProfileForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     self._user_id_kwargs = kwargs['pk']
    #     self._user_age = UserProfileModel.objects.get('user_id')
    #     super().__init__(*args, **kwargs)

    class Meta:

        model = User
        fields = 'username', 'email', 'first_name', 'last_name', 'age', 'city', 'gender', 'avatar_pic'

        # widgets = {
        #     'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'self.labels'}),
        #     'gender': forms.SelectMultiple(attrs={'class': 'form-control'}),
        #     'city': forms.TextInput(attrs={'class': 'form-control', }),
        #     'signature': forms.Textarea(attrs={'class': 'card', }),
        #
        # }


class SignUpBaseForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        field_classes = {'username': UsernameField}


class AboutPageForm(forms.ModelForm):
    class Meta:
        model = AboutData
        fields = '__all__'
