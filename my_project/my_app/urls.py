from django.urls import path
from . import views
from .views import SignUpView, CustomLoginView
urlpatterns = [
    path('', views.doctor_list, name='doctor_list'),
    path('doctor/<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login')
]