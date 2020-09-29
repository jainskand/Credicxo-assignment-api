from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsTeacherOrSuperAdmin,IsSuperAdmin
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class TeacherView(APIView):
    #authentication_classes = [JWTAuthentication,SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated,IsSuperAdmin]
    def get(self, format=None):

        teachers = TeacherProfile.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)


class StudentView(APIView):
    """
    A class based view for creating and fetching student records
    """
    #authentication_classes = [JWTAuthentication,SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated,IsTeacherOrSuperAdmin]
    def get(self, format=None):
        """
        Get all the student records
        :return: Returns a list of student records
        """
        students = StudentProfile.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def studentDetail(request,pk=None):
    if pk==None:
        if 'student' in [group.name for group in request.user.groups.all()]:
            student = get_object_or_404(StudentProfile,user=request.user)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        else:
            return Response('login as student to access', status=status.HTTP_400_BAD_REQUEST)
    else:
        groups = [group.name for group in request.user.groups.all()]
        if len(set(groups)&set(('teacher','supeadmin')))!=0:
            student = get_object_or_404(StudentProfile,pk=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        else:
            return Response({"detail":"You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)


'''
{
    "user":{
        "username":"hello",
        "first_name":"hello",
        "last_name":"Singh",
        "email":"hello@gmail.com",
        "password":"abcd"
    },
    "subject":"Physics"
}
'''
