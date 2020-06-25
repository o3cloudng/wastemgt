from django import forms

from .models import Client


class ClientForm(forms.ModelForm):
    # email = forms.EmailField(required=True)
    # first_name = forms.CharField(max_length=30)
    # last_name = forms.CharField(max_length=50)
    class Meta:
        model = Client
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        # fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    # def save(self, commit=True):
    #     user = super().save(commit=True)

    #     user.email = self.cleaned.data['email']
    #     user.first_name = self.cleaned.data['first_name']
    #     user.last_name = self.cleaned.data['last_name']

    #     if commit:
    #         user.save()
    #     return user

