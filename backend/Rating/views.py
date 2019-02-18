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
from Rating.models import Post, UserProfile
from Rating.serializers import PostSerializer, UserSerializer, UserProfileSerializer


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


class PostList(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self):
        pass


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
