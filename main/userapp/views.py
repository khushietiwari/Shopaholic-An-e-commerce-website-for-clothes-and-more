import random
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from .models import OTP
from django.contrib.auth import authenticate, login, logout


# ================= REGISTER =================
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('userapp:register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.is_active = False
        user.save()

        otp_code = str(random.randint(100000, 999999))

        OTP.objects.create(
            user=user,
            otp=otp_code
        )

        send_mail(
            subject='Shopaholic Email Verification',
            message=f'Your OTP is {otp_code}',
            from_email='noreply@shopaholic.com',
            recipient_list=[email],
        )

        request.session['otp_user_id'] = user.id
        messages.success(request, 'OTP sent to your email')
        return redirect('userapp:verify_otp')

    return render(request, 'userapp/register.html')


# ================= VERIFY OTP =================
def verify_otp(request):
    user_id = request.session.get('otp_user_id')

    if not user_id:
        return redirect('userapp:register')

    user = User.objects.get(id=user_id)

    if request.method == 'POST':
        entered_otp = request.POST.get('otp')

        otp_obj = OTP.objects.filter(user=user, otp=entered_otp).first()

        if otp_obj:
            user.is_active = True
            user.save()
            otp_obj.delete()

            messages.success(request, 'Account verified! Please login.')
            return redirect('userapp:login')
        else:
            messages.error(request, 'Invalid OTP')

    return render(request, 'userapp/verify_otp.html')


# ================= LOGIN =================
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user and user.is_active:
            login(request, user)

            # ✅ set voice flag
            request.session['just_logged_in'] = True

            return redirect('shop:home')

        elif user and not user.is_active:
            messages.error(request, 'Please verify your email using OTP first.')

        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'userapp/login.html')



# ================= LOGOUT =================
def logout_view(request):
    logout(request)
    return redirect('shop:home')
