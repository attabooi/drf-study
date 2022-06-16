from django.shortcuts import render
from django.contrib.auth import login, authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt

class UserApiView(APIView):
    # 로그인
    @csrf_exempt # 한번하고 지우기
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return Response({"message": "로그인 성공!!"}, status=status.HTTP_200_OK)

