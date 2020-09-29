'''from django.urls import path,include

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('teacher',views.TeacherView)

urlpatterns = [
        path('',include(router.urls))
]
'''
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('teachers/', views.TeacherView.as_view()),
    path('students/',views.StudentView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
