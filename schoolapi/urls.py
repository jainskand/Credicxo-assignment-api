from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('teachers/', views.TeacherView.as_view()),
    path('students/',views.StudentView.as_view()),
    path('studentdetail/',views.studentDetail),
    path('studentdetail/<int:pk>/',views.studentDetail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
