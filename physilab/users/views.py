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
            return redirect('landing_page') 
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
            return redirect('profile_view')  
    else:
        user_form = UserUpdateForm(instance=request.user)

    context = {
        'user_form': user_form,
    }
    return render(request, 'profile_edit.html', context)

def logout_view(request):
    logout(request)
    messages.info(request, "Anda telah keluar.")
    return redirect('index') 


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
        volume = float(request.POST.get('volume'))
        mol = float(request.POST.get('mol'))
        temperature = float(request.POST.get('suhu'))  

        R = 8.314 
        pressure = mol * R * temperature / volume 
        result = f"{pressure:.2f} Pa"

        CalculationHistory.objects.create(
            user=request.user,
            volume=volume,
            mol=mol,
            temperature=temperature,
            result=result
        )

        history = CalculationHistory.objects.filter(user=request.user).order_by('-created_at')

        context = {
            'result': result,
            'history': history,
            'volume': volume,
            'mol': mol,
            'temperature': temperature,
        }
        return render(request, 'calc.html', context)
    else:
        history = CalculationHistory.objects.filter(user=request.user).order_by('-created_at')
        return render(request, 'calc.html', {'history': history})

def clear_history(request):
    CalculationHistory.objects.filter(user=request.user).delete()
    return redirect('calc')