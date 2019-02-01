from django.contrib.auth.models import User
from rest_framework import serializers

from .models import UserProfile, Post, Comment


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("username", "is_superuser", "is_staff", "date_joined")


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"
