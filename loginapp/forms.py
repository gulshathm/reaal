from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class CompanyRegistrationForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'address', 'email']

    # Add user registration fields
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )
        company = super().save(commit=False)
        company.user = user
        if commit:
            company.save()
        return company

# class ClientRegistrationForm(UserCreationForm):
#     registration_count = forms.IntegerField(min_value=1, label='Number of Registrations')
#
#     class Meta:
#         model = User
#         fields = ['username', 'password1', 'password2', 'registration_count']
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         if commit:
#             user.save()
#         return user
class ClientRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']