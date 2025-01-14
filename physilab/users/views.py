from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import CustomUserCreationForm, UserUpdateForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import CalculationHistory

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Akun berhasil dibuat!")
            return redirect('login')
        else:
            messages.error(request, "Terjadi kesalahan. Mohon periksa kembali form.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('landing_page')  # Use 'landing_page' instead of 'home'
        else:
            messages.error(request, "Username or password is incorrect.")
    return render(request, 'login.html')

def profile_view(request):
    return render(request, 'profile_view.html', {'user': request.user})

def profile_edit(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('profile_view')  # Redirect back to the profile view page
    else:
        user_form = UserUpdateForm(instance=request.user)

    context = {
        'user_form': user_form,
    }
    return render(request, 'profile_edit.html', context)

def logout_view(request):
    logout(request)
    messages.info(request, "Anda telah keluar.")
    return redirect('index')  # Update to the desired logout redirect page


from django.shortcuts import render, redirect

def index_page(request):
    return render(request, 'index.html')

def landing_page(request):
    return render(request, 'landing.html')

def calc_page(request):
    return render(request, 'calc.html')

def material_page(request):
    return render(request, 'material.html')

def calculate_pressure(request):
    if request.method == 'POST':
        # Retrieve input values from the form
        volume = float(request.POST.get('volume'))
        mol = float(request.POST.get('mol'))
        suhu = float(request.POST.get('suhu'))

        # Perform the calculation (example: Ideal Gas Law)
        pressure = mol * 8.314 * suhu / volume  # P = nRT/V
        result = f"{pressure:.2f} Pa"

        # Save the new calculation to the history
        CalculationHistory.objects.create(user=request.user, result=result)

        # Retrieve all calculations for this user
        history = CalculationHistory.objects.filter(user=request.user).order_by('created_at')

        # Pass the result and history to the template
        context = {
            'result': result,
            'history': history,
        }
        return render(request, 'calc.html', context)
    else:
        # On GET request, fetch all history without performing a new calculation
        history = CalculationHistory.objects.filter(user=request.user).order_by('-created_at')
        return render(request, 'calc.html', {'history': history})

def clear_history(request):
    # Delete all calculation history for the logged-in user
    CalculationHistory.objects.filter(user=request.user).delete()
    # Redirect back to the calculator page (or wherever you want)
    return redirect('calc')