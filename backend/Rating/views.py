from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView


# posts/
from Rating.forms import UserForm
from Rating.models import Post, UserProfile, Comment
from Rating.serializers import PostSerializer, UserSerializer, UserProfileSerializer, CommentSerializer


class UserDetailsList(ListAPIView):
    serializer_class_User = UserSerializer
    serializer_class_UserProfile = UserProfileSerializer

    def get_queryset_User(self):
        return User.objects.all()

    def get_queryset_UserProfile(self):
        return UserProfile.objects.all()

    def list(self, request, *args, **kwargs):
        users = self.serializer_class_User(self.get_queryset_User(), many=True)
        user_profiles = self.serializer_class_UserProfile(self.get_queryset_UserProfile(), many=True)
        return Response({"users": users.data,
                         "user_profiles": user_profiles.data
                         })


class PostList(ListAPIView):
    serializer_class_Post = PostSerializer
    serializer_class_Comment = CommentSerializer

    def get_queryset_Post(self):
        return Post.objects.all()

    def get_queryset_Comment(self):
        return Comment.objects.all()

    def list(self, request, *args, **kwargs):
        posts = self.serializer_class_Post(self.get_queryset_Post(), many=True)
        comments = self.serializer_class_Comment(self.get_queryset_Comment(), many=True)
        return Response({"posts": posts.data,
                         "comments": comments.data
                         })


class SignUpView(View):
    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(new_user)
            # redirect, or however you want to get to the main view
            return HttpResponseRedirect('main.html')
        else:
            form = UserForm()
            return render(request, 'adduser.html', {'form': form})
