# accounts/views.py

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Register View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Hesabınız başarıyla oluşturuldu, {user.username}!")
            return redirect('home')
        else:
            messages.error(request, "Kayıt başarısız. Lütfen bilgilerinizi kontrol edin.")
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Hoş geldiniz, {user.username}!")

            # Kullanıcı türüne göre yönlendirme
            if user.is_superuser:
                return redirect('dashboard:admin-dashboard')  # Yönetici dashboard
            """
            elif user.is_staff:
                return redirect('dashboard:employee-dashboard')  # Çalışan dashboard
            else:
                messages.error(request, "Geçersiz kullanıcı türü.")
                return redirect('accounts:login')  # Eğer kullanıcı türü belirlenmemişse login sayfasına yönlendirme
                """
        else:
            messages.error(request, "Geçersiz kullanıcı adı veya şifre!")
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})
# Home View
@login_required
def home(request):
    return render(request, 'home.html')
