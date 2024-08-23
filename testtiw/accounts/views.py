from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm, StudentProfileForm, OrganizerProfileForm
from .models import User, Student, Organizer


def index(request):
    return render(request, 'accounts/index.html')

def role_selection(request):
    return render(request, 'accounts/role_selection.html')

def register(request):
    role = request.GET.get('role')
    
    if role not in ['student', 'organizer']:
        return redirect('role_selection')
    
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            if role == 'student':
                user.is_student = True
                user.save()
                student_form = StudentProfileForm(request.POST)
                if student_form.is_valid():
                    student_profile = student_form.save(commit=False)
                    student_profile.user = user
                    student_profile.save()
            elif role == 'organizer':
                user.is_organizer = True
                user.save()
                organizer_form = OrganizerProfileForm(request.POST)
                if organizer_form.is_valid():
                    organizer_profile = organizer_form.save(commit=False)
                    organizer_profile.user = user
                    organizer_profile.save()

            # เปลี่ยนเส้นทางไปยังหน้าเข้าสู่ระบบหลังจากสมัครสมาชิกเสร็จ
            return redirect('login')
    else:
        user_form = UserRegistrationForm()
        if role == 'student':
            profile_form = StudentProfileForm()
        else:
            profile_form = OrganizerProfileForm()

    return render(request, 'accounts/register.html', {'user_form': user_form, 'profile_form': profile_form, 'role': role})


from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = CustomLoginForm

    def get_success_url(self):
        user = self.request.user
        if user.is_student:
            return '/student-dashboard/'  # URL สำหรับนักศึกษา
        elif user.is_organizer:
            return '/organizer-dashboard/'  # URL สำหรับผู้จัดกิจกรรม
        else:
            return '/home/'  # URL เริ่มต้น


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def student_dashboard(request):
    if request.user.is_student:
        return render(request, 'accounts/student_dashboard.html')
    else:
        return redirect('role_selection')

@login_required
def organizer_dashboard(request):
    if request.user.is_organizer:
        return render(request, 'accounts/organizer_dashboard.html')
    else:
        return redirect('role_selection')