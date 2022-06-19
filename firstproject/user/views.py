from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt

from django.db.models import F

from user.models import UserProfile
from blog.models import Article

from user.serializers import UserSerializer




class UserApiView(APIView):   
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'head', 'post']
    

        #사용자 정보 조회

    def get(self, request):
        user = request.user
        return Response(UserSerializer(user).data)

    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        print(username)
        print(password)

        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return Response({"message": "로그인 성공!!"}, status=status.HTTP_200_OK)

