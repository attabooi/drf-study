import json
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from blog.models import Article, Category
from user.models import User

from user.serializers import UserSerializer

from drf_project.permissions import RegistedMoreThanThreeDaysUser

class ArticleView(APIView): # CBV 방식
    # permission_classes = [permissions.AllowAny] # 누구나 view 조회 가능
    # permission_classes = [permissions.IsAdminUser] # admin만 view 조회 가능
    # permission_classes = [permissions.IsAuthenticated] # 로그인 된 사용자만 view 조회 가능
    permission_classes = [RegistedMoreThanThreeDaysUser]
    def get(self, request):
        user = request.user
        all_users = User.objects.all()

        return Response(UserSerializer(all_users, many=True).data)
        
    def post(self, request):
        
        title = request.data.get('title','')
        categories = request.data.get('categories','')
        body = request.data.get('body','')
        
        

        print(title)
        print(categories)
        print(body)
        if len(title) <= 5:
            return Response({'error': 'title이 5글자 이하라면 글을 작성할 수 없습니다.'})

        if len(body) <= 20:
            return Response({'error': '글 길이가 20글자 이하라면 글을 작성할 수 없습니다.'})

        if categories is not None:
            create_article = Article.objects.create(
            author = request.user,
            title = title,
            body = body
        )
            print(categories)
            categories = Category.objects.get(category=categories)


            
            create_article.save()

            return Response({'message': '글 작성 성공!'})
        else:
            return Response({'error': '카테고리를 지정해주세요.'})


    def put(self, request):
        return Response({'message': 'put method!!'})

    def delete(self, request):
        return Response({'message': 'delete method!!'})
