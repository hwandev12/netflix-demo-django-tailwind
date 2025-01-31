from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name='login'),
    path("register/", register_view, name='register'),
    path("signup/", step_1_of_1, name='step_1_of_1'),
    path("signup/planform/", step_2_of_1, name='step_2_of_1'),
    path("signup/registration/", step_1_of_2, name='step_1_of_2'),
    path("signup/regform/", step_2_of_2, name='step_2_of_2'),
    path("signup/paymentPicker/", step_1_of_3, name='step_1_of_3'),
    path("signup/creditoption/", step_2_of_3, name='step_2_of_3'),
    path("router/", router, name='router'),
    path("session-logout/", session_logout, name='session_logout'),
]