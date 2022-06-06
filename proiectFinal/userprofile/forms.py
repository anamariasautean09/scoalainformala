from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput


class NewAccountForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'first_name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'last_name', 'class': 'form-control'}),
            'username': TextInput(attrs={'placeholder': 'username', 'class': 'form-control'}),
            'email': TextInput(attrs={'placeholder': 'email address', 'class': 'form-control'}),
        }

    # def __init__(self, *args, **kargs):
    #     super(NewAccountForm, self).__init__(*args, **kargs)
    #     self.fields['email'].widget.attrs['class'] = 'form-control'


    def clean(self):
        field_data = self.cleaned_data
        email_value = field_data.get('email')
        if User.objects.filter(email=email_value).exists():
            self._errors['email'] = self.error_class(['Email-ul deja exista! Te rugam sa adaugi un email unic!'])
        return field_data