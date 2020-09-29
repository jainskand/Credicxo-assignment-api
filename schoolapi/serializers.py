from rest_framework import serializers, status
from .models import *
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','password')
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = TeacherProfile
        fields = ('user', 'subject',)

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        group = Group.objects.get_or_create(name ='teacher')[0]
        user.groups.add(group)
        user.save()
        teacher, created = TeacherProfile.objects.update_or_create(user=user,
                            subject=validated_data.pop('subject'))
        return teacher

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = StudentProfile
        fields = ('user', 'student_class',)

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        group = Group.objects.get_or_create(name ='student')[0]
        user.groups.add(group)
        user.save()
        student, created = StudentProfile.objects.update_or_create(user=user,
                            student_class=validated_data.pop('student_class'))
        return student
