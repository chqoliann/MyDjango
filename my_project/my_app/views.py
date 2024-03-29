from django.shortcuts import render
from .models import Doctor, DoctorTime
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView as BaseLoginView


class CustomLoginView(BaseLoginView):
    success_url = reverse_lazy('doctor_list')
    template_name = 'login.html'

class SignUpView(generic    .CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('doctor_list')
    template_name = 'signup.html'


def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor_list.html', {'doctors': doctors})


def doctor_detail(request, doctor_id):
    doctor = Doctor.objects.get(pk=doctor_id)
    available_times = DoctorTime.objects.filter(doctor=doctor)
    return render(request, 'doctor_detail.html', {'doctor': doctor, 'available_times': available_times})


def home(request):
    show_signup_button = True
    return render(request, 'home.html', {'show_signup_button': show_signup_button})
