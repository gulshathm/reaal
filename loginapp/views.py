
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Company,Client


def frontpage(request):
    return render(request,'front.html')
# Form for registering a company
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

# Company registration view
def register(request):
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CompanyRegistrationForm()
    return render(request, 'register.html', {'form': form})

# Login view
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')  # Redirect to a success page.
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Home view for company
def home(request):
    if not request.user.is_authenticated or not hasattr(request.user, 'company'):
        return redirect('login')

    company = request.user.company
    clients = Client.objects.filter(company=company)
    return render(request, 'home.html', {'clients': clients})

class ClientRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# Client registration view
def client_register(request):
    if request.method == 'POST':
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            company = request.user.company
            Client.objects.create(user=user, company=company)
            return redirect('client_login')
    else:
        form = ClientRegistrationForm()
    return render(request, 'client_register.html', {'form': form})

# Client login view
def client_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('client_home')  # Redirect to client home/dashboard
    else:
        form = AuthenticationForm()
    return render(request, 'client_login.html', {'form': form})

def client_home(request):
    return render(request,'client_home.html')