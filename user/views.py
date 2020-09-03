from django.shortcuts import render, redirect
from .models import User
from .forms import RegistrationForm, UserRoleForm
from django.contrib import messages
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import logging
from product.models import Product


logger = logging.getLogger(__name__)

# Create your views here.
def register(request):
    form = RegistrationForm()
    user_role_form = UserRoleForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        user_role_form = UserRoleForm(request.POST)

        if form.is_valid() and user_role_form.is_valid():
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            role = user_role_form.cleaned_data['role']

            user = User.objects._create_user(
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password,
            )

            user.save()

            user_role = user_role_form.save(commit=False)
            user_role.user = user
            user_role.role = role
            user_role.save()
            logger.info('New account created by {0} {1} with email:{2} as {3}'.format(
                first_name, last_name, email, role
            ))
            messages.success(request, 'Hi ' + first_name + '!, your account is created successfully! Please login')
            return redirect('/')
    context = {
        'form': form,
        'user_role_form': user_role_form,
    }
    return render(request, 'user/register.html', context)

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            if user.user_role.role == 'Customer':
                return redirect('product:product_list')
            elif user.user_role.role == 'Vendor':
                return redirect('user:home')
        else:
            messages.warning(request, 'Email or Password is incorrect, try again')
    context = {}
    return render(request, 'user/login.html', context)

def user_logout(request):
    logout(request)
    return redirect('user:login')

@login_required(login_url='user:login')
def home(request):
    context = {}
    return render(request, 'user/home.html', context)
