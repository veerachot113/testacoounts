from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('role-selection/', role_selection, name='role_selection'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('student-dashboard/', student_dashboard, name='student_dashboard'),
    path('organizer-dashboard/', organizer_dashboard, name='organizer_dashboard'),
    path('register/', register, name='register'),
    
]