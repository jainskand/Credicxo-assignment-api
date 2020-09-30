from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from .permissions import IsTeacherOrSuperAdmin,IsSuperAdmin
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group, User
from rest_framework_simplejwt.tokens import RefreshToken

class TeacherView(APIView):
    """
    A class based view for creating and fetching teachers records
    """
    #authentication_classes = [JSessionAuthentication, BasicAuthentication]
    #permissions so only super admin users can access methods
    permission_classes = [IsAuthenticated,IsSuperAdmin]
    def get(self, format=None):
        """
        Get all the teachers records
        :return: Returns a list of teachers records
        """
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
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
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
    '''function view to access detail of a student'''
    if pk==None:
        # to get detail of logged-in user(student)
        if 'student' in [group.name for group in request.user.groups.all()]:
            student = get_object_or_404(StudentProfile,user=request.user)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        else:
            #if loggedin user is not student throw HTTP_400_BAD_REQUEST
            return Response({"detail":'login as student to access'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        #to get detail of any student by providing pk
        #only teachers or superadmins can access
        groups = [group.name for group in request.user.groups.all()]
        if len(set(groups)&set(('teacher','supeadmin')))!=0:
            student = get_object_or_404(StudentProfile,pk=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        else:
            #if user is not teacher or superadmin throwing HTTP_403_FORBIDDEN
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

@api_view(["POST"])
@permission_classes([AllowAny])
def registration(request):
    serializer = UserSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    user = serializer.save()
    group = Group.objects.get_or_create(name ='superadmin')[0]
    user.groups.add(group)
    refresh = RefreshToken.for_user(user)
    res = {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }
    return Response(res, status.HTTP_201_CREATED)

@api_view(["POST"])
@permission_classes([AllowAny])
def teacherRegistration(request):
    serializer = TeacherSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    user = serializer.save()
    refresh = RefreshToken.for_user(user)

    res = {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }
    return Response(res, status.HTTP_201_CREATED)

@api_view(["POST"])
@permission_classes([AllowAny])
def studentRegistration(request):
    serializer = StudentSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    user = serializer.save()
    refresh = RefreshToken.for_user(user)
    res = {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }
    return Response(res, status.HTTP_201_CREATED)
