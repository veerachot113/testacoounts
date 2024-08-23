from django.contrib.auth.models import AbstractUser,User
from django.db import models

# Choices สำหรับคำนำหน้า
TITLE_CHOICES = [
    ('นาย', 'นาย'),
    ('นาง', 'นาง'),
    ('นางสาว', 'นางสาว'),
]

# Choices สำหรับคณะ
FACULTY_CHOICES = [
    ('วิทยาศาสตร์', 'วิทยาศาสตร์'),
    ('คณะเกษตรศาสตร์', 'คณะเกษตรศาสตร์'),
    ('คณะวิศวกรรมศาสตร์', 'คณะวิศวกรรมศาสตร์'),
    ('คณะศิลปศาสตร์', 'คณะศิลปศาสตร์'),
    ('คณะเภสัชศาสตร์', 'คณะเภสัชศาสตร์'),
    ('คณะบริหารศาสตร์', 'คณะบริหารศาสตร์'),
    ('วิทยาลัยแพทยศาสตร์และการสาธารณสุข', 'วิทยาลัยแพทยศาสตร์และการสาธารณสุข'),
    ('คณะนิติศาสตร์', 'คณะนิติศาสตร์'),
    ('คณะรัฐศาสตร์', 'คณะรัฐศาสตร์'),
    ('คณะพยาบาลศาสตร์', 'คณะพยาบาลศาสตร์'),
]

# Choices สำหรับประเภททุน
SCHOLARSHIP_CHOICES = [
    ('กยศ', 'กยศ'),
    ('ทุน', 'ทุน'),
    ('ทุน-กยศ', 'ทุน-กยศ'),
]

# Custom User Model
class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_organizer = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # ปรับชื่อ related_name เพื่อหลีกเลี่ยงการชนกัน
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',  # ปรับชื่อ related_name เพื่อหลีกเลี่ยงการชนกัน
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_query_name='user',
    )

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    title = models.CharField(max_length=10, choices=TITLE_CHOICES,default='0')
    faculty = models.CharField(max_length=100, choices=FACULTY_CHOICES,default='0')
    number_of_credits_required = models.IntegerField(default=0)  # จำนวนหน่วยกิตที่ต้องการ
    number_of_credits_available = models.IntegerField(default=0)  # จำนวนหน่วยกิตที่มีอยู่
    scholarship_type = models.CharField(max_length=50, choices=SCHOLARSHIP_CHOICES,default='0')

    def __str__(self):
        return f"{self.title} {self.user.first_name} {self.user.last_name}"

class Organizer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    title = models.CharField(max_length=10, choices=TITLE_CHOICES ,default='0')
    faculty = models.CharField(max_length=100, choices=FACULTY_CHOICES,default='0')

    def __str__(self):
        return f"{self.title} {self.user.first_name} {self.user.last_name}"
