from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

#Teaacher model having one to one relationship with User model
class TeacherProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name = 'teacher')
    subject = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

#Student model having one to one relationship with User model
class StudentProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name = 'student')
    student_class = models.PositiveSmallIntegerField(validators=[MaxValueValidator(12),MinValueValidator(1)])

    def __str__(self):
        return self.user.username
