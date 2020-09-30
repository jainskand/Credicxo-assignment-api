from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    #endpoint to access list of teachers or to add new teachers
    path('teachers/', views.TeacherView.as_view()),
    #endpoint to access list of students or to add new Students
    path('students/',views.StudentView.as_view()),
    #endpoint to get detail of student account
    path('studentdetail/',views.studentDetail),
    path('studentdetail/<int:pk>/',views.studentDetail),
    # endpoint to register/sign-up as superadmin
    path('registeradmin/',views.registration),
    # endpoint to register/sign-up as student
    path('registerstudent/',views.studentRegistration),
    # endpoint to register/sign-up as teacher
    path('registerteacher/',views.teacherRegistration),
]

urlpatterns = format_suffix_patterns(urlpatterns)
