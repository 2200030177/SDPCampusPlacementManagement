from django.contrib.auth import authenticate, login
from django.http import request
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def home(request):
    return render(request, "home.html")

def register(request):
    return render(request, 'register.html')

def aboutus(request):
    return render(request, "aboutus.html")

def service(request):
    return render(request, "services.html")

def contact(request):
    return render(request, "contact.html")
def signupsignin(request):
    return render(request, "signupsignin.html")
def cosignupsignin(request):
    return render(request, "cosignupsignin.html")
def student_verification(request):
    if request.method == 'POST':
        id_number = request.POST.get('id_number', '')
        if len(id_number) > 4:
            # If the ID number length is greater than 4, redirect to student signup/signin page
            return redirect('signupsignin')
        else:
            # If the ID number length is less than or equal to 4, redirect to company signup/signin page
            return redirect('cosignupsignin')
    return render(request, 'student_verification.html')

def company_verification(request):
    if request.method == 'POST':
        id_number = request.POST.get('id_number', '')
        if len(id_number) > 4:
            # If the ID number length is greater than 4, redirect to student signup/signin page
            return redirect('signupsignin')
        else:
            # If the ID number length is less than or equal to 4, redirect to company signup/signin page
            return redirect('cosignupsignin')
    return render(request, 'company_verification.html')


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import User


def signupsignin(request):
    if request.method == "POST":
        action = request.POST.get('action')

        if action == 'signup':
            name = request.POST.get('name')
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')

            # Create the user using Django's default User model
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = name
            user.save()

            # Authenticate user after signup
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home page after successful signup
            else:
                # Handle authentication failure
                return render(request, "signupsignin.html", {'error_message': 'Failed to authenticate'})

        elif action == 'signin':
            username = request.POST.get('username')
            password = request.POST.get('password')

            # Authenticate user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home page after successful signin
            else:
                # Handle authentication failure
                return render(request, "signupsignin.html", {'error_message': 'Invalid credentials'})

    # Handle GET request (if any)
    return render(request, "signupsignin.html")
