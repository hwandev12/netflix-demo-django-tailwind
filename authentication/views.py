from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import User, AccountCard
from django.contrib.auth.hashers import make_password
from django.contrib.sessions.backends.db import SessionStore
from django.contrib import messages
from django.db import transaction

from django.db.models import Q


def login_view(request):
    if request.user.is_authenticated:
        return redirect("/main/")
    if request.method == "POST":
        session_email = request.session.get("email", None)
        login_field = request.POST.get("login_field")
        password = request.POST.get("password")
        try:
            if not session_email:
                user = User.objects.get(Q(phone_number=login_field) | Q(email=login_field))
                if user is not None and user.check_password(password):
                    login(request, user)
                return redirect("/main/")
            else:
                messages.warning(request, "Uzur siz to'liq ro'yhatdan o'tmagansiz!")
                print('salom')
        except User.DoesNotExist:
            pass
    return render(request, "auth/login.html")


def register_view(request):
    if request.method == "POST":
        login_field = request.POST.get("login_field")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        full_name = request.POST.get("full_name")
        try:
            if password == confirm_password:
                if not User.objects.filter(
                    Q(email=login_field) | Q(phone_number=login_field)
                ).exists():
                    user = User.objects.create(
                        email=login_field,
                        fullName=full_name,
                        password=make_password(password),
                    )
                    login(request, user)
                    return redirect("/main/")
        except Exception as e:
            print(e)
    return render(request, "auth/register.html")


def step_1_of_1(request):
    if request.user.is_authenticated:
        return redirect("/main/")
    session_email = request.session.get("email", None)
    return render(request, "auth/step_1/1.html", { "session": True if session_email else False })


def step_2_of_1(request):
    session_email = request.session.get("email", None)
    return render(request, "auth/step_1/2.html", { "session": True if session_email else False })


def step_1_of_2(request):
    session_email = request.session.get("email", None)
    if session_email:
        user = User.objects.filter(email=session_email).exists()
        if user:
            return redirect("/auth/signup/creditoption/")
    return render(request, "auth/step_2/1.html", { "session": True if session_email else False })


def step_2_of_2(request):
    session_email = request.session.get("email", None)
    user = User.objects.filter(email=session_email).exists()
    if user:
        return redirect("/auth/signup/paymentPicker/")
    elif request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        User.objects.create(email=email, password=make_password(password))
        request.session["email"] = email
        return redirect("/auth/signup/paymentPicker/")
    return render(request, "auth/step_2/2.html", { "session": True if session_email else False })


def step_1_of_3(request):
    session_email = request.session.get("email", None)
    if not session_email:
        return redirect("/auth/signup/planform/")
    else:
        user = User.objects.filter(email=session_email).exists()
        if not user:
            return redirect("/auth/signup/planform/")
    return render(request, "auth/step_3/1.html", { "session": True if session_email else False })


def step_2_of_3(request):
    session_email = request.session.get("email", None)
    if not session_email:
        return redirect("/auth/signup/planform/")
    else:
        user = User.objects.filter(email=session_email).exists()
        session_user = User.objects.get(email=session_email)
        if request.method == 'POST':
            card_number = request.POST.get("card_number")
            expiration_date = request.POST.get("expiration_date")
            cvv = request.POST.get("cvv")
            name = request.POST.get("name")
            c = AccountCard(
                user=session_user,
                name=name,
                number=card_number,
                expiry_date=expiration_date,
                cvv=cvv
            )
            with transaction.atomic():
                c.save()
                request.session.flush()
                if session_user is not None:
                    login(request, session_user)
                return redirect("/main")
        if not user:
            return redirect("/auth/signup/planform/")
    return render(request, "auth/step_3/2.html", { "session": True if session_email else False })


def router(request):
    try:
        session_email = request.session["email"]
        user = User.objects.filter(email=session_email).exists()
        if user:
            return redirect("/auth/signup/paymentPicker/")
    except KeyError:
        pass
    return redirect("/auth/signup/")


def session_logout(request):
    session_email = request.session.get("email", None)
    if session_email:
        User.objects.filter(email=session_email).delete()
    request.session.flush()
    return redirect("/auth/signup/")



# encrypt -- okajonim --> sakdfhja*&^&*^&*FYDsjhGHJGJ8768768

# decrypt -- sakdfhja*&^&*^&*FYDsjhGHJGJ8768768 --> parol
