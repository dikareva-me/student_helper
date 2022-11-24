from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Task

from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class TasksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = "__all__"
